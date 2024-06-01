import datetime

def show_time():
         now = datetime.datetime.now()
         current_time = now.strftime("%Y-%m-%d %H:%M:%S")
         print("Current Time:", current_time)

def main():
         while True:
             user_input = input("Type 'show time' to see the current time, or 'exit' to quit: ").strip().lower()
             if user_input == 'show time':
                 show_time()
             elif user_input == 'exit':
                 print("Exiting the program. Goodbye!")
                 break
             else:
                 print("Invalid command. Please try again.")

if __name__ == "__main__":
 main()