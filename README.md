# AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: JEVIN PAWAN FERNANDES

*INTERN ID*: CT04DZ1493

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

**Project Description

For this project, I decided to work on something practical: automating the process of creating reports. Normally, whenever we analyze a dataset, we spend a lot of time writing down the summary, preparing graphs, and then putting everything together in a nice-looking document. It’s repetitive and can be boring. So I thought – why not make Python do all of that for me automatically?

The idea is simple:

Take some data from a file (like a CSV).

Run a script that reads and analyzes the data.

Generate a ready-made PDF report with both tables and graphs.

This way, no matter what dataset I use, the script can produce a formatted report within seconds.

Tools I Used

I used Visual Studio Code (VS Code) as my coding environment because it’s comfortable and has a built-in terminal for running Python scripts. For the code itself, I relied on a few important Python libraries:

Pandas → for reading and analyzing the dataset.

Matplotlib → to create charts and graphs from the data.

ReportLab → to generate the final PDF document in a structured format.

These three libraries together made the whole workflow smooth – one for data, one for visuals, and one for report creation.

How It Works

Here’s how my script works step by step:

Reading the data – The script first loads a CSV file into a pandas DataFrame. This allows me to handle the dataset in a tabular format, just like Excel, but inside Python.

Analyzing the data – I used the describe() function from pandas, which gives a quick statistical summary (like mean, min, max, quartiles, and standard deviation). This summary gives an overview of the data without having to look through every single value.

Creating a visualization – To make the report more meaningful, I added a histogram for one of the numeric columns. For example, if the dataset has student marks, the histogram shows how the marks are distributed. If it’s sales data, it shows how often certain sales ranges occur.

Generating the PDF – This is the fun part. Using ReportLab, I created a structured PDF that starts with a title, then adds the summary statistics, and finally includes the chart image I generated earlier. When the script finishes, it saves the file as Automated_Report.pdf.

So basically, from raw data to a professional-looking report happens automatically with just one script run.

Why This is Useful

This project might seem small, but it has huge practical applications. Imagine:

A teacher can instantly generate student performance reports.

A business can automatically create monthly sales reports.

A researcher can summarize experimental data without spending hours formatting documents.

It saves time, reduces human error, and produces consistent results every time.

My Experience

Working on this project was honestly fun because I could see everything come together – data analysis, visualization, and reporting. At first, I thought making a PDF with Python would be complicated, but once I explored ReportLab, it felt like building a Word file but programmatically. VS Code also made debugging easier since I could run the code and preview outputs quickly.

The best part? Now if I ever get a new dataset, I don’t need to start from scratch. I just drop the file in, run my script, and I have a clean PDF report ready to share.

Conclusion

In short, this project is all about making life easier when dealing with repetitive reporting tasks. Using Python with pandas, matplotlib, and reportlab, I managed to automate the entire process of reading data, analyzing it, visualizing it, and exporting it into a PDF report.

It’s like having a personal data assistant that prepares reports for me on demand — and I definitely see myself extending this further with more graphs and maybe even interactive dashboards in the future.**

#OUTPUT

<img width="1111" height="777" alt="Image" src="https://github.com/user-attachments/assets/51ec9307-820a-44b1-837e-47b0dbaa74c6" />
<img width="1078" height="667" alt="Image" src="https://github.com/user-attachments/assets/6dd9bbe6-56d3-48e0-9d9c-b233355bb05a" />
<img width="1050" height="691" alt="Image" src="https://github.com/user-attachments/assets/d2ea9446-d197-46a5-880c-1aa12d5bce96" />
