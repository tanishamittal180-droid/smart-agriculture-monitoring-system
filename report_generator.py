from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


class ReportGenerator:

    def generate(
        self,
        report_data
    ):

        doc = SimpleDocTemplate(
            "outputs/farm_report.pdf"
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "AgriSense AI Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 12)
        )

        for key, value in report_data.items():

            content.append(
                Paragraph(
                    f"{key}: {value}",
                    styles["BodyText"]
                )
            )

        doc.build(content)