"""
Sample geographic and climate dataset for the GeoResearch Assistant.
"""

GEO_CLIMATE_DATA = [
    # Temperature and Climate
    "The Amazon rainforest has a tropical climate with high temperatures averaging 27°C (80°F) year-round and receives about 2,300 mm of rainfall annually.",
    "Antarctica is the coldest continent on Earth, with temperatures reaching as low as -89.2°C (-128.6°F) at Vostok Station. It contains about 90% of the world's ice.",
    "The Sahara Desert is the world's largest hot desert, spanning 9 million square kilometers across North Africa. Temperatures can exceed 50°C (122°F) during the day.",
    "Iceland has a subarctic oceanic climate with cool summers averaging 10-13°C and relatively mild winters due to the Gulf Stream. It experiences volcanic and geothermal activity.",
    "The Mediterranean climate is characterized by hot, dry summers and mild, wet winters. This climate is found around the Mediterranean Sea and in parts of California, Chile, South Africa, and Australia.",
    
    # Geography and Landforms
    "Mount Everest, located in the Himalayas on the border between Nepal and Tibet, is the Earth's highest mountain above sea level at 8,848.86 meters (29,031.7 feet).",
    "The Great Barrier Reef off the coast of Queensland, Australia, is the world's largest coral reef system, stretching over 2,300 kilometers and visible from space.",
    "The Nile River is traditionally considered the longest river in the world at approximately 6,650 kilometers, flowing through eleven countries in northeastern Africa before emptying into the Mediterranean Sea.",
    "The Mariana Trench in the western Pacific Ocean is the deepest oceanic trench on Earth, reaching a maximum depth of about 10,994 meters (36,070 feet) at Challenger Deep.",
    "Lake Baikal in Siberia, Russia, is the world's deepest and oldest freshwater lake, containing about 23% of the world's fresh surface water and reaching depths of 1,642 meters.",
    
    # Countries and Regions
    "Brazil is the largest country in South America, covering 8.5 million square kilometers. It contains the Amazon rainforest and has a population of over 210 million people.",
    "Russia is the world's largest country by land area, spanning 17.1 million square kilometers across Eastern Europe and Northern Asia. It has 11 time zones.",
    "Singapore is a small island city-state in Southeast Asia with an area of only 728 square kilometers. Despite its size, it has become one of the world's major financial centers.",
    "Canada is the second-largest country in the world by total area at 9.98 million square kilometers. It has the longest coastline in the world at over 202,000 kilometers.",
    "The Netherlands is a low-lying country in Western Europe, with about 26% of its area below sea level. It is famous for its extensive system of dikes and polders.",
    
    # Climate Phenomena
    "El Niño is a climate pattern characterized by unusually warm ocean temperatures in the Equatorial Pacific, affecting weather patterns globally and typically occurring every 2-7 years.",
    "Monsoons are seasonal wind patterns that bring heavy rainfall to South and Southeast Asia, typically from June to September. India receives about 80% of its annual rainfall during the summer monsoon.",
    "The polar vortex is a large area of low pressure and cold air surrounding both poles. When it weakens or becomes distorted, it can bring extremely cold air to mid-latitude regions.",
    "Trade winds are persistent easterly winds found in the tropics, blowing from the subtropical high-pressure belts toward the equatorial low-pressure belt. They were crucial for historical sailing routes.",
    "The greenhouse effect is the process by which gases in Earth's atmosphere trap heat, keeping the planet warm enough to support life. However, increased greenhouse gas emissions are causing global warming.",
    
    # Oceans and Water Bodies
    "The Pacific Ocean is the largest and deepest ocean, covering about 165 million square kilometers (approximately 46% of the world's ocean surface) and containing more than half of Earth's free water.",
    "The Dead Sea, bordering Jordan and Israel, is one of the world's saltiest bodies of water with a salinity of about 34%. Its surface is 430 meters below sea level, the lowest point on Earth's land surface.",
    "The Arctic Ocean is the smallest and shallowest of the world's five major oceans, covering approximately 14 million square kilometers. It is largely covered by sea ice that is shrinking due to climate change.",
    "The Mediterranean Sea is nearly landlocked, connected to the Atlantic Ocean through the Strait of Gibraltar. It has been central to the history of Western civilization.",
    "The Amazon River discharges more water than any other river, approximately 209,000 cubic meters per second. It accounts for about 20% of the total water discharged into oceans by rivers worldwide.",
    
    # Ecosystems and Biomes
    "The tundra biome is characterized by extremely cold temperatures, low biodiversity, and a layer of permanently frozen subsoil called permafrost. It is found in the Arctic and high mountain regions.",
    "Tropical rainforests cover less than 6% of Earth's land surface but contain more than half of the world's plant and animal species. They play a crucial role in regulating global climate.",
    "The savanna is a grassland ecosystem with scattered trees, found in tropical and subtropical regions. The African savanna is home to large herbivores like elephants, zebras, and giraffes.",
    "Coral reefs are marine ecosystems formed by colonies of coral polyps. They support about 25% of all marine species and provide coastal protection, but are threatened by ocean warming and acidification.",
    "The boreal forest (taiga) is the world's largest terrestrial biome, stretching across northern North America, Europe, and Asia. It consists mainly of coniferous trees and experiences long, cold winters.",
    
    # Climate Change
    "Global average temperatures have increased by approximately 1.1°C since the pre-industrial era, primarily due to increased greenhouse gas emissions from human activities.",
    "Sea levels are rising at an accelerating rate, currently about 3.3 millimeters per year, threatening coastal communities and small island nations. This is caused by thermal expansion and melting ice.",
    "The Arctic is warming at twice the global average rate, a phenomenon known as Arctic amplification. This leads to sea ice loss, permafrost thawing, and affects global weather patterns.",
    "Deforestation, particularly in tropical regions, contributes about 10% of global greenhouse gas emissions and reduces Earth's capacity to absorb carbon dioxide from the atmosphere.",
    "Extreme weather events, including heatwaves, droughts, floods, and hurricanes, are becoming more frequent and intense due to climate change, affecting millions of people worldwide."
]


def get_dataset() -> list:
    """
    Get the geographic and climate dataset.
    
    Returns:
        List of text documents about geography and climate.
    """
    return GEO_CLIMATE_DATA


def get_dataset_info() -> dict:
    """
    Get information about the dataset.
    
    Returns:
        Dictionary with dataset statistics.
    """
    return {
        'num_documents': len(GEO_CLIMATE_DATA),
        'topics': [
            'Temperature and Climate',
            'Geography and Landforms',
            'Countries and Regions',
            'Climate Phenomena',
            'Oceans and Water Bodies',
            'Ecosystems and Biomes',
            'Climate Change'
        ]
    }