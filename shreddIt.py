from PIL import Image
import os
import random
import math
import argparse

def shred_image(image_path, puzzle_number, num_shreds):
    
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = os.path.join(script_dir, f'puzzle{puzzle_number}')

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = Image.open(image_path)

    width, height = img.size

    shred_width = width // num_shreds

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    shreds = []
    for i in range(num_shreds):
        left = i * shred_width
        right = (i + 1) * shred_width
        shred = img.crop((left, 0, right, height))
        shreds.append(shred)

    num_rotated = num_shreds // 3  
    rotated_indices = random.sample(range(num_shreds), num_rotated)
    for i in rotated_indices:
        angle = math.pi
        shreds[i] = shreds[i].rotate(math.degrees(angle))

    # Shuffle the shreds randomly
    random.shuffle(shreds)

    for i, shred in enumerate(shreds):
        shred.save(os.path.join(output_dir, f'shred_{i + 1}.jpg'))

    print(f'{num_shreds} pieces shredded, shuffled, and saved to {output_dir}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Shred and manipulate an image.')

    parser.add_argument('--image_path', type=str, required=True, help='Path to the input image')
    parser.add_argument('--puzzle_number', type=int, required=True, help='Puzzle number to create the output directory')
    parser.add_argument('--num_shreds', type=int, default=7, help='Number of shreds (default: 7)')

    args = parser.parse_args()

    shred_image(args.image_path, args.puzzle_number, args.num_shreds)
