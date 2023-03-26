import random
import cv2

class GAEmotionTransition:
    def __init__(self, emotions, population_size, num_generations, mutation_rate):
        self.emotions = emotions
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.population = []
        self.fitness_scores = {}
        self.best_individual = None
        self.fitness_score = None

    def create_initial_population(self):
        for i in range(self.population_size):
            video = []
            for j in range(10):
                video.append(random.choice(list(self.emotions.keys())))
            self.population.append(video)

    def fitness(self, video_emotion):
        video_filename = self.emotions[video_emotion]
        cap = cv2.VideoCapture(video_filename, cv2.CAP_FFMPEG)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        rating = int(input("Please rate this video on a scale of 1 to 10: "))
        return rating

    def evaluate_population(self):
        for individual in self.population:
            fitness_score = 0
            for video_emotion in individual:
                fitness_score += self.fitness(video_emotion)
            self.fitness_scores[str(individual)] = fitness_score


    def select_best_individuals(self):
        best_individuals = sorted(self.population, key=lambda x: self.fitness_scores[str(x)], reverse=True)[:int(self.population_size/2)]
        if len(best_individuals) == 0:
            best_individuals = [max(self.population, key=lambda x: self.fitness_scores[str(x)])]
        self.best_individual = best_individuals[0]
        self.fitness_score = self.fitness_scores[str(self.best_individual)]
        return best_individuals


    def crossover(self, video1, video2):
        split_point = random.randint(0, len(video1))
        child1 = video1[:split_point] + video2[split_point:]
        child2 = video2[:split_point] + video1[split_point:]
        return child1, child2

    def mutation(self, video):
        mutation_point = random.randint(0, len(video)-1)
        video[mutation_point] = random.choice(list(self.emotions.keys()))
        return video

    def create_next_generation(self, best_individuals):
        next_generation = []
        for i in range(self.population_size-len(best_individuals)):
            parent1, parent2 = random.sample(best_individuals, 2)
            child1, child2 = self.crossover(parent1, parent2)
            if random.random() < self.mutation_rate:
                child1 = self.mutation(child1)
            if random.random() < self.mutation_rate:
                child2 = self.mutation(child2)
            next_generation.append(child1)
            next_generation.append(child2)
        self.population = best_individuals + next_generation

    def run(self):
        self.create_initial_population()
        for generation in range(self.num_generations):
            print(f"Generation {generation}")
            self.evaluate_population()
            best_individuals = self.select_best_individuals()
            self.create_next_generation(best_individuals)

        print("The best individual is:", self.best_individual)
        print("The fitness score is:", self.fitness_score)


# Define the available emotions and their corresponding videos
emotions = {
    "happy": "~EVA/PMV/eva_110_smile.mp4",
    "sad": "~EVA/PMV/eva011_eng.mp4",
    "angry": "~EVA/PMV/eva011_eng.mp4",
    "neutral": "~EVA/PMV/eva_110_smile.mp4"
}

# Define the genetic algorithm parameters
population_size = 4
num_generations = 2
mutation_rate = 0.5

# Create the GA object
ga = GAEmotionTransition(emotions, population_size, num_generations, mutation_rate)
ga.run()