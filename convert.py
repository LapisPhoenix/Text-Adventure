import PIL.Image
import os
 

def convert(input_path, output_path):
    i = 0
    for file in os.listdir(input_path):
        img_flag = True
        
        try:
            img = PIL.Image.open(os.path.join(input_path, file))
            img_flag = True
        except:
            print(os.path.join(input_path, file), "Unable to find image ");
        
        width, height = img.size
        aspect_ratio = height/width
        new_width = 160
        new_height = aspect_ratio * new_width * 0.55
        img = img.resize((new_width, int(new_height)))
        
        img = img.convert('L')
        
        chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", ".", "#"]
        
        pixels = img.getdata()
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        
        with open(os.path.join(output_path, f"{i}.txt"), "w") as f:
            f.write(ascii_image)
        i += 1

    j = 0

    for file in os.listdir(output_path):
        with open("animations.py", "a") as f:
            if j == 0:
                f.write("walk = [")
                j += 1
            with open(os.path.join(output_path, file), "r") as f2:
                f.write(f'"""{f2.read()}""",')

    with open("animations.py", "a") as f:
        f.write("]")

if __name__ == "__main__":
    input_path = input("Enter the path to the folder with images: ")
    output_path = input("Enter the path to the folder where you want to save the ASCII images: ")
    convert(input_path, output_path)