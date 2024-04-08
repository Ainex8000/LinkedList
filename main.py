class WebsiteNavigator:
    # Constructor
    def __init__(self):
        # List of websites
        self.websites = [    
        "https://www.google.com",
        "https://www.facebook.com",
        "https://www.youtube.com",
        "https://www.twitter.com",
        "https://www.instagram.com",
        "https://www.linkedin.com",
        "https://www.reddit.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.netflix.com",
        "https://www.spotify.com",
        "https://www.amazon.com",
        "https://www.nytimes.com",
        "https://www.bbc.com",
        "https://www.wikipedia.org",
        "https://www.apple.com",
        "https://www.microsoft.com",
        "https://www.python.org",
        "https://www.coursera.org",
        "https://www.uat.edu",]
        # Current index
        self.current_index = -1

    # Display the list of websites
    def display_list(self):
        print("Website List:")
        for index, website in enumerate(self.websites, start=1):
            print(f"{index}. {website}")
        print()

    # Go forward
    def go_forward(self):
        # Check if there are websites ahead
        if self.current_index < len(self.websites) - 1:
            self.current_index += 1
            print(f"Opening: {self.websites[self.current_index]}")
        # If the user is at the last website, display a message
        else:
            print("Already at the last website.")

    # Go backward
    def go_backward(self):
        # Check if there are websites behind
        if self.current_index > 0:
            self.current_index -= 1
            print(f"Opening: {self.websites[self.current_index]}")
        # If the user is at the first website, displays an error message
        else:
            print("Already at the first website.")

    # Add a website to the list
    def add_website(self, website):
        # Append the website to the list
        self.websites.append(website)
        print(f"{website} added to the list.")

    # Delete a website from the list by using the index number
    def delete_website(self, index):
        # Check if the index is valid
        try:
            deleted_website = self.websites.pop(index - 1)
            print(f"{deleted_website} deleted from the list.")
        # If the index is invalid, displays an error message
        except IndexError:
            print("Invalid index.")

    # Find a website in the list by searching the website's url
    def find_website(self, website):
        # Check if the website is in the list and informs the user that the website is found
        if website in self.websites:
            print(f"{website} found in the list.")
        # If the website is not in the list, informs the user that the website is not found
        else:
            print(f"{website} not found in the list.")

    # Menu
    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Display the list")
            print("2. Go forward and display the webpage")
            print("3. Go backward and display the webpage")
            print("4. Add another item to the list")
            print("5. Delete an item from the list")
            print("6. Find an item in the list")
            print("7. Exit")

            # Get user's choice
            choice = input("Enter your choice (1-7): ")

            # Perform the choice
            if choice == '1':
                # Display the list
                self.display_list()
            elif choice == '2':
                # Go forward
                self.go_forward()
            elif choice == '3':
                # Go backward
                self.go_backward()
            elif choice == '4':
                # Add a website
                website = input("Enter the website to add: ")
                self.add_website(website)
            elif choice == '5':
                # Delete a website
                index = int(input("Enter the index to delete: "))
                self.delete_website(index)
            elif choice == '6':
                # Find a website
                website = input("Enter the website to find: ")
                self.find_website(website)
            elif choice == '7':
                # Exit the program
                print("Exiting program.")
                break
            # Invalid choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")


# Main function
if __name__ == "__main__":
    # Create a WebsiteNavigator object
    navigator = WebsiteNavigator()
    # Call the menu method
    navigator.menu()
