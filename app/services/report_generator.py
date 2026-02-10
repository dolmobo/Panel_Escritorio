import os
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics.charts.legends import Legend

class ReportService:
    @staticmethod
    def encabezado_y_pie(canvas, doc):
        canvas.saveState()
        ancho, alto = A4
        
        # Línea superior
        canvas.setStrokeColor(colors.dodgerblue)
        canvas.setLineWidth(2)
        canvas.line(1.5*cm, alto - 2.8*cm, ancho - 1.5*cm, alto - 2.8*cm)

        canvas.setFont('Helvetica-Bold', 14)
        canvas.setFillColor(colors.darkblue)
        canvas.drawString(1.5*cm, alto - 1.5*cm, "CYBERSPRINT STATS")
        
        canvas.setFont('Helvetica', 10)
        canvas.setFillColor(colors.black)
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
        canvas.drawRightString(ancho - 1.5*cm, alto - 1.5*cm, f"Fecha: {fecha}")

        canvas.setStrokeColor(colors.dodgerblue)
        canvas.setLineWidth(1)
        canvas.line(1.5*cm, 2*cm, ancho - 1.5*cm, 2*cm)
        
        canvas.setFont('Helvetica', 8)
        canvas.drawString(1.5*cm, 1.5*cm, "Informe generado por CyberSprint Desktop App")
        canvas.drawRightString(ancho - 1.5*cm, 1.5*cm, f"Página {doc.page}")
        
        canvas.restoreState()

    @staticmethod
    def generar_informe_perfil(nombre_archivo, datos, promedios=None):
        doc = SimpleDocTemplate(nombre_archivo, pagesize=A4, 
                                rightMargin=1.5*cm, leftMargin=1.5*cm, 
                                topMargin=3*cm, bottomMargin=2.5*cm)
        estilos = getSampleStyleSheet()
        
        estilo_titulo = ParagraphStyle(
            'TituloCyber',
            parent=estilos['Title'],
            fontSize=18,
            textColor=colors.dodgerblue,
            alignment=TA_CENTER,
            spaceAfter=20
        )

        guion = []

        # --- LOGO ---
        ruta_logo = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logo.png")
        if os.path.exists(ruta_logo):
            try:
                img = Image(ruta_logo, width=4*cm, height=2.5*cm, kind='proportional')
                img.hAlign = 'CENTER'
                guion.append(img)
                guion.append(Spacer(1, 0.5*cm))
            except: pass

        # --- TÍTULOS ---
        guion.append(Paragraph(f"ESTADÍSTICAS DE USUARIO: {datos.get('username', 'Usuario')}", estilo_titulo))
        guion.append(Spacer(1, 0.5*cm))
        guion.append(Paragraph("Comparativa de rendimiento frente a la media global del servidor.", estilos['Normal']))
        guion.append(Spacer(1, 1*cm))

        # --- TABLA DE DATOS ---
        data = [
            ["MÉTRICA", "TU VALOR"],
            ["Récord Máximo", f"{datos.get('record', 0)}"],
            ["Partidas Jugadas", f"{datos.get('partidas_totales', 0)}"],
            ["Saltos Totales", f"{datos.get('saltos_totales', 0)}"],
            ["Monedas", f"{datos.get('monedas', 0)}"],
        ]

        tabla = Table(data, colWidths=[8*cm, 8*cm], rowHeights=0.8*cm)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.aliceblue, colors.white])
        ]))
        
        guion.append(tabla)
        guion.append(Spacer(1, 1.5*cm))

        # --- GRÁFICO COMPARATIVO ---
        guion.append(Paragraph("Análisis Comparativo (Tú vs Media)", estilos['Heading2']))
        guion.append(Spacer(1, 10))

        # Llamamos a la función de gráfico pasándole ambos datos
        grafico = ReportService._crear_grafico_comparativo(datos, promedios)
        guion.append(grafico)
        
        guion.append(Spacer(1, 1*cm))

        doc.build(guion, onFirstPage=ReportService.encabezado_y_pie, onLaterPages=ReportService.encabezado_y_pie)

    @staticmethod
    def _crear_grafico_comparativo(datos, promedios):
        """Genera gráfico de barras agrupadas: Usuario vs Media"""
        
        # Si no hay promedios (error de red), usamos ceros para que no falle
        if not promedios:
            promedios = {'monedas': 0, 'saltos_totales': 0, 'record': 0, 'partidas_totales': 0}

        d = Drawing(450, 250) # Lienzo grande
        
        # Serie 1: Datos del Usuario
        data_user = [
            datos.get('monedas', 0),
            datos.get('saltos_totales', 0),
            datos.get('record', 0),
            datos.get('partidas_totales', 0)
        ]
        
        # Serie 2: Promedios Globales
        data_avg = [
            promedios.get('monedas', 0),
            promedios.get('saltos_totales', 0),
            promedios.get('record', 0),
            promedios.get('partidas_totales', 0)
        ]

        # Configuración del gráfico
        bc = HorizontalBarChart()
        bc.x = 100
        bc.y = 50
        bc.height = 160
        bc.width = 300
        
        # ¡Aquí pasamos las dos listas!
        bc.data = [data_user, data_avg]
        
        # Colores: Azul para ti, Gris para la media
        bc.bars[0].fillColor = colors.dodgerblue
        bc.bars[1].fillColor = colors.lightgrey
        
        # Configuración de Ejes
        bc.valueAxis.valueMin = 0
        bc.categoryAxis.categoryNames = ['Monedas', 'Saltos', 'Récord', 'Partidas']
        bc.categoryAxis.labels.fontName = 'Helvetica'
        
        # Etiquetas numéricas en las barras
        bc.barLabelFormat = '%d'
        bc.barLabels.nudge = 10
        
        # --- LEYENDA (Para saber quién es quién) ---
        leyenda = Legend()
        leyenda.alignment = 'right'
        leyenda.x = 420
        leyenda.y = 220
        leyenda.colorNamePairs = [
            (colors.dodgerblue, 'TU USUARIO'), 
            (colors.lightgrey, 'MEDIA GLOBAL')
        ]
        
        d.add(bc)
        d.add(leyenda)
        
        return d
    
    # ... (Mantén los imports y el método encabezado_y_pie igual) ...

    @staticmethod
    def generar_informe_ranking(nombre_archivo, titulo_reporte, nombre_columna_dato, lista_datos):
        """
        Genera un PDF con una tabla de ranking y un gráfico del Top 5.
        lista_datos: Lista de diccionarios [{'nombre': 'User', 'valor': 100}, ...]
        """
        doc = SimpleDocTemplate(nombre_archivo, pagesize=A4, 
                                rightMargin=1.5*cm, leftMargin=1.5*cm, 
                                topMargin=3*cm, bottomMargin=2.5*cm)
        estilos = getSampleStyleSheet()
        
        # Estilos (Reutilizamos los tuyos)
        estilo_titulo = ParagraphStyle('TituloCyber', parent=estilos['Title'], fontSize=18, textColor=colors.dodgerblue, alignment=TA_CENTER, spaceAfter=20)
        
        guion = []

        # --- LOGO ---
        ruta_logo = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logo.png")
        if os.path.exists(ruta_logo):
            try:
                img = Image(ruta_logo, width=4*cm, height=2.5*cm, kind='proportional')
                img.hAlign = 'CENTER'
                guion.append(img)
                guion.append(Spacer(1, 0.5*cm))
            except: pass

        # --- TÍTULO ---
        guion.append(Paragraph(f"RANKING GLOBAL: {titulo_reporte.upper()}", estilo_titulo))
        guion.append(Paragraph(f"Listado completo de jugadores ordenados por {titulo_reporte.lower()}.", estilos['Normal']))
        guion.append(Spacer(1, 0.5*cm))

        # --- GRÁFICO TOP 5 (Para mantener la estética visual) ---
        guion.append(Paragraph(f"Top 5 Mejores Jugadores", estilos['Heading2']))
        guion.append(Spacer(1, 10))
        
        # Cogemos solo los 5 primeros para el gráfico
        top_5 = lista_datos[:5]
        if top_5:
            grafico = ReportService._crear_grafico_ranking(top_5)
            guion.append(grafico)
        
        guion.append(Spacer(1, 1*cm))

        # --- TABLA DE DATOS ---
        # Cabecera
        data_tabla = [["POSICIÓN", "JUGADOR", nombre_columna_dato.upper()]]
        
        # Filas
        for i, item in enumerate(lista_datos):
            pos = str(i + 1)
            nombre = item.get('nombre', 'Desconocido')
            valor = str(item.get('valor', 0))
            data_tabla.append([pos, nombre, valor])

        # Estilo de tabla (El mismo azul profesional)
        tabla = Table(data_tabla, colWidths=[3*cm, 8*cm, 5*cm], repeatRows=1)
        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.aliceblue, colors.white])
        ]))
        
        guion.append(tabla)
        
        # Construir
        doc.build(guion, onFirstPage=ReportService.encabezado_y_pie, onLaterPages=ReportService.encabezado_y_pie)

    @staticmethod
    def _crear_grafico_ranking(datos_top_5):
        """Gráfico de barras horizontales para el Top 5"""
        d = Drawing(450, 150)
        
        nombres = [d['nombre'] for d in datos_top_5]
        valores = [d['valor'] for d in datos_top_5]
        
        # Invertimos para que el Top 1 salga arriba en el gráfico horizontal
        nombres.reverse()
        valores.reverse()

        bc = HorizontalBarChart()
        bc.x = 100
        bc.y = 20
        bc.height = 120
        bc.width = 300
        bc.data = [valores]
        
        bc.valueAxis.valueMin = 0
        bc.categoryAxis.categoryNames = nombres
        bc.categoryAxis.labels.fontName = 'Helvetica'
        bc.categoryAxis.labels.fontSize = 9
        
        bc.bars[0].fillColor = colors.dodgerblue
        bc.barLabelFormat = '%d'
        bc.barLabels.nudge = 10
        
        d.add(bc)
        return d