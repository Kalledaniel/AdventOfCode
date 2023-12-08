class MapCon:
    def __init__(self, destination, source, len): 
        self.destination = destination
        self.source = source
        self.len = len
    
    def checkme(self, number):
        min = self.source
        max = (self.source + self.len)

        if number >= min and number < max:
            return True
        else: 
            return False
        
    def get_destination(self, number):
        return self.destination - self.source + number
        
    def print(self):
        print(self.destination, self.source, self.len)

    def new_ranges(self, rmin, rmax):
        min = self.source
        max = (self.source + self.len)
        new_ranges = [[rmin, rmax]]
        to = self.destination - self.source
        # case 1: rmin is in range but not rmax
        if rmin >= min and rmin < max and rmax > max:
            newrange = [[rmin + to, max + to], [max+1, rmax]]
            return newrange
        # case 2: rmax is in range but not rmin
        if rmax >= min and rmax < max and rmin < min:
            newrange = [[rmin, min-1], [min + to, rmax + to]]
            return newrange
        # case 3: rmin and rmax are in range
        if rmin >= min and rmin < max and rmax > min and rmax <= max:
            newrange = [[rmin + to, rmax + to]]
            return newrange
        # case 4: rmin and rmax are not in range
        if rmin < min and rmax > max:
            newrange = [[rmin, min-1], [min + to, max + to], [max+1, rmax]]
            return newrange

        return new_ranges
        # if rmin < min and rmax > max:
        #     new_min = min
        #     new_max = max

class Range:
    def __init__(self, seed, range):
        self.min = seed
        self.max = seed + range

    def get_number(self):
        return self.number

    def print(self):
        print(self.number)

def merge_ranges(input_list):
    if not input_list:
        return []

    # Sort the input list based on the minimum values
    sorted_ranges = sorted(input_list, key=lambda x: x[0])

    # Initialize the result list with the first range
    result = [sorted_ranges[0]]

    for current_range in sorted_ranges[1:]:
        # Check if the current range overlaps with the last range in the result
        if current_range[0] <= result[-1][1]:
            # Merge the ranges if there is an overlap
            result[-1][1] = max(result[-1][1], current_range[1])
        else:
            # If there is no overlap, add the current range to the result
            result.append(current_range)

    return result

def get_text(txt):
    game = []
    read_file = open(txt, "r")
    for line in read_file:
        game.append(line.rstrip('\n'))  # Remove newline characters
    read_file.close()
    return game 

def get_maps(text):
    seeds = []
    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []
    arrays = [seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]
    index = 0
    arrays[0].append(text[0].split(":")[1].split())
    breaker = ["seed" , "seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]

    for line in text:
        if line.split(":")[0] == "seeds" or line == "":
            continue
        elif line in breaker:
            index += 1
        else:
            numbers = line.split()
            map = MapCon(int(numbers[0]), int(numbers[1]), int(numbers[2]))
            arrays[index].append(map)
    return arrays

def part1():
    print("start day 5")
    text = get_text("day5data.txt")

    maps = get_maps(text)

    seeds = maps[0]
    seeds = seeds[0]



    locations = []
    print(seeds)

    for seed in seeds:
      
        current_location = int(seed)
        for map in maps[1:]:
            for i in map:
                if i.checkme(current_location):
                    current_location = i.get_destination(current_location)
                    break
        locations.append(int(current_location))
    
    print(min(locations))

def part2():
    # 114197007 to low
    # 114197007 
    # 505901489 i dont know

    print("start day 5 Part 2")
    # text = get_text("day5datatest.txt")
    text = get_text("day5data.txt")
    maps = get_maps(text)
    seeds = maps[0]
    seeds = seeds[0]
    mins = []
    
    min_max = []
    for i in range(len(seeds)):
        if i % 2 == 0:
          min_max.append([int(seeds[i]), int(int(seeds[i+1]) + int(seeds[i]))-1])
    
    current_min_maxes = [] 
    iter = 1
    for number in min_max:
        print("doing number: ", number)
        current_min_maxes = [number]
        new_min_maxes = []  
        for map in maps[1:]:            
            new_min_maxes = []
            for n in current_min_maxes:
                splited = False
                for i in map:
                    new = i.new_ranges(int(n[0]), int(n[1]))
                    if new != [n]:
                        splited = True
                        for j in new:
                            if j not in new_min_maxes:
                                new_min_maxes.append(j)    
                if splited == False:
                    new_min_maxes.append(n)
            current_min_maxes = new_min_maxes
            current_min_maxes = merge_ranges(current_min_maxes) 
        smallest = 99999999999999999999
        for i in current_min_maxes:
          if i[0] < smallest:
            smallest = i[0]
        mins.append(smallest)
        print("iter = " + str(iter))
        iter += 1
        print(current_min_maxes)
    print(mins)
    print(min(mins))
def test():
    print("start day 5") 
    # [5,25], [5,15], [5,10], [5,5], [5,0], [0,25], [0,15], [0,10], [0,5],      
    # list = [[5,25]]
    # map = MapCon(0, 10, 10) # 5-15
    # map2 = MapCon(0, 100, 10) # 0-10
    # map3 = MapCon(1000, 0, 10) # 0-10
    # map4 = MapCon(15, 100, 20) # 0-10
    # map5 = MapCon(1000, 1000, 5) # 0-10
    # map6 = MapCon(1000, 20, 1) # 0-10
    # maps = [[map,map2], [map3,map4], [map5,map6]]
# test()
# part1()
part2()