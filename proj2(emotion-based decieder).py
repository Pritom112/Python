import random


def decide_recommendation(emotion):
    recommendations = {
        "happy": ["The Pursuit of Happyness", "Up", "The Grand Budapest Hotel"],
        "sad": ["The Fault in Our Stars", "Schindler's List", "Grave of the Fireflies"],
        "excited": ["The Avengers", "Inception", "Mad Max: Fury Road"],
        "calm": ["The Secret Life of Walter Mitty", "Amélie", "Spirited Away"],
        "surprised": ["The Sixth Sense", "Fight Club", "The Usual Suspects"]
    }

    if emotion.lower() in recommendations:
        return random.choice(recommendations[emotion.lower()])
    else:
        return "Sorry, I don't have recommendations for that emotion."


if __name__ == "__main__":
    print("Hi!")
    emotion = input("Enter your current emotion (happy, sad, excited, calm, surprised): ")

    recommendation = decide_recommendation(emotion)

    print(f"\nBased on your emotion ({emotion}), I recommend you to watch: {recommendation}")

    input("\nPress Enter to exit...")
