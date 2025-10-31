data = input("Enter some text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(data + "\n")

print("Data written to output.txt successfully.")

#Append additional data to the same file
more_data = input("Enter additional text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(more_data + "\n")

print("Additional data appended successfully.")

#Read and display the final content of the file
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
