class CropGrowth:
    
    def get_stage(
        self,
        soil_moisture
    ):

        if soil_moisture > 80:
            return "🌾 Harvest Stage"

        elif soil_moisture > 65:
            return "🌼 Flowering Stage"

        elif soil_moisture > 50:
            return "🌿 Vegetative Stage"

        elif soil_moisture > 35:
            return "🌱 Germination Stage"

        return "🌰 Seed Stage"