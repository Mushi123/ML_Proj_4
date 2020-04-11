# To run the tester.py please make sure to follow the following instructions:

1. Put an `images` folder in the same directory as the tester.py with the 101 by 101 images to test on
2. Have file named `labels.csv` with a header row followed by the labels of the images in the `images` folder, in order. Have this file in the same folder as `tester.py`
3. Have the weights `celegans.npy` in the same folder as `tester.py`
4. Run the command `python tester.py images` when the current working directory has `tester.py` on the top level
5. The accuracy will be printed out