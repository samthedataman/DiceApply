import time
import sys
import random

messages = [
    "✨ Dream job is just around the corner...",
    "💼 Polishing your resume to shine brighter...",
    "🚀 Fasten your seatbelt, opportunities ahead!",
    "💡 Lighting up your future career path...",
    "🍀 Fortune favors the bold. Almost there...",
    "📈 Preparing to skyrocket those applications!",
]

reminders = [
    "📝 Don't forget to set up your Dice account at https://www.dice.com/dashboard/login!",
    "📂 Make sure to upload the resume you're using for these roles.",
    "💻 Pro tip: Tech roles love a polished GitHub profile—got yours ready?",
    "🕵️ Update your keywords for tech roles to boost your chances!",
    "📨 Check your inbox frequently—responses may come quicker than you think!",
]

emojis = ["🌟", "🚀", "🎯", "📈", "🍀", "⚡", "💼", "💰"]


def fun_loading_screen():
    print("🚀 Launching the AutoApplyBot... Hold tight!\n")
    for i in range(1, 101):
        time.sleep(0.05)

        # Choose random reminders and messages at key milestones
        if i % 25 == 0:
            reminder = random.choice(reminders)
            emoji = random.choice(emojis)
            print(f"\n{emoji} {reminder}")

        # Dynamically update the progress with emojis
        bar = f"[{'=' * (i // 10)}{' ' * (10 - i // 10)}] {i}%"
        sys.stdout.write(f"\r{random.choice(emojis)} Progress: {bar}")
        sys.stdout.flush()

    print("\n🎉 Done! You're ready to start applying effortlessly!")
    print("💼 Get ready to land those tech roles and unlock new opportunities!")


# Run the fun loading screen
if __name__ == "__main__":
    fun_loading_screen()
