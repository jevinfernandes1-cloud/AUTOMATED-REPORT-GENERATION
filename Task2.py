import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(input_file, output_file):
    # 1. Read data
    df = pd.read_csv(input_file)

    # 2. Analyze data
    summary = df.describe(include='all').fillna('')

    # 3. Create PDF
    pdf = SimpleDocTemplate(output_file, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # --- Header Section ---
    elements.append(Paragraph("Automated Data Report", styles['Title']))
    elements.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal']))
    elements.append(Spacer(1, 20))

    # --- Summary Table ---
    elements.append(Paragraph("Dataset Summary", styles['Heading2']))
    data = [summary.columns.to_list()] + summary.values.tolist()
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
    ]))
    elements.append(table)
    elements.append(Spacer(1, 20))

    # --- Charts Section ---
    elements.append(Paragraph("Charts & Visualizations", styles['Heading2']))

    # Example chart: Age distribution
    plt.figure(figsize=(4,3))
    df['Age'].plot(kind='hist', bins=5, color='skyblue', edgecolor='black')
    plt.title("Age Distribution")
    plt.xlabel("Age")
    chart_file = "age_hist.png"
    plt.savefig(chart_file)
    plt.close()
    elements.append(Image(chart_file, width=400, height=250))
    elements.append(Spacer(1, 20))

    # Example chart: Score by Name
    plt.figure(figsize=(4,3))
    df.plot(x='Name', y='Score', kind='bar', legend=False, color='green')
    plt.title("Scores by Student")
    plt.ylabel("Score")
    chart_file2 = "scores_bar.png"
    plt.savefig(chart_file2)
    plt.close()
    elements.append(Image(chart_file2, width=400, height=250))

    # --- Build PDF ---
    pdf.build(elements)
    print(f"Report saved as {output_file}")

if __name__ == "__main__":
    sample_csv = "sample_data.csv"
    sample_pdf = "report.pdf"

    # Create sample dataset
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Age": [25, 30, 35, 40, 28],
        "Score": [88, 92, 79, 85, 95]
    }
    pd.DataFrame(data).to_csv(sample_csv, index=False)

    # Generate enhanced PDF report
    generate_report(sample_csv, sample_pdf)
