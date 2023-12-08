


# Image Unshredder
## Overview

This repository contains a Mathematica notebook designed to re-stitch shredded images. Utilizing advanced edge-matching methods and a sophisticated sorting algorithm, the tool effectively solves puzzles where an image is shredded into vertical slices. Each slice can be randommly rotated, and all the shredded slices are shuffled at the end. The notebook can take in any image split into any number of slices and stitch the image back together

## Process
1) Load all images.
2) Convert them to grayscale to reduce number of color channels that require matching at the edges.
3) Create an 2D array which contains left edge, flipped left edge, right edge, flipped right edge for all images.
4) Use squared euclidean distance between all possible edges in the array, taken 2 at a time,  to find how close two edges are.
5) Zero out all distances that are calculated between edges of same image as presence of white border on one edge of image can cause errors in the next step by reporting really short distances.
6) If there are 'k' pieces, find the indices of the k-1 least, distinct, non-zero distances from the array. This will give us all the required edge pairs and the orientations the edges pair in. (Distinct coz two edges can be paired in different orientation by changing order)
7) Using the above array of indices found, find the order of images. Start with the first where the First is one of the images that only pairs with one of its edges. Subsequent images are found by checking which image pairs with the previously found image recursively.
8)Using the sequence(order of images found above), completely reorder the ordered pairs(indices) of edges in the order that they would appear on the final image for stitching.
9) Using the rearranged indices found above, find which images need to be flipped (orientation). For the first image, if right or right flipped edge is used for pairing, do not flip. Else flip. For all subsequent images, if they use left or left flipped edge for pairing do not flip. Else flip.
10) Return the sequence along with the orientation and pass them to ImageAssemble function to see the stitched image. 

## Usage and 
1) Download any image of your choice
2) Run the shreddIt.py to split the image. Adjust the arguments accordingly specifying path to input image, name of output directory (puzzle number) and number of pieces. 
```bash
$ python shreddIt.py \
--image_path <path to image> \
--puzzle_number <puzzle number> \
--num_shreds <number of shreds>
```
3) Open the notebook and change the range of the following function from 10,12 to the required. (These are the puzzle numbers to stitch)
![image](https://github.com/Auc7us/ECE533Final/assets/35758803/ad393808-a82e-44e6-82d7-1cafc64d4313)

## Examples
![image](https://github.com/Auc7us/ECE533Final/assets/35758803/2b7c7a5b-3552-4ae4-963f-3209da0ce389)




