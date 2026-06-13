class RecommendationEngine:
    
    def generate(
        self,
        moisture,
        temperature,
        water
    ):

        recommendations = []

        if moisture < 40:
            recommendations.append(
                "Increase irrigation."
            )

        if temperature > 40:
            recommendations.append(
                "Heat stress detected."
            )

        if water < 30:
            recommendations.append(
                "Refill water tank."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Farm conditions are optimal."
            )

        return recommendations