from farm_analytics.analytics_engine import AnalyticsEngine

analytics = AnalyticsEngine()

print("\n===== FARM REPORT =====\n")

report = analytics.generate_report()

for key, value in report.items():
    print(f"{key}: {value}")

analytics.close()