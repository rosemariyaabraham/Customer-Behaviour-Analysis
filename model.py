from flask import Flask,render_template,url_for
import matplotlib.image as mpimg
import numpy as np
import cv2
from skimage.feature import hog
import matplotlib.pyplot as plt
import glob
from sklearn.svm import LinearSVC, SVC
from sklearn.preprocessing import StandardScaler
from skimage.feature import hog
from sklearn.model_selection import train_test_split, GridSearchCV
import imageio
import numpy as np
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.heatmaps import HeatmapsOnImage

app = Flask(__name__)

@app.route('/')
def projects():
    return render_template("custom1.html")

@app.route('/about1')
def about():
    return render_template("about.html")
@app.route('/team1')
def team():
    return render_template("ourteam.html")    
@app.route('/work1')
def working():
    return render_template("works.html")
@app.route('/analyst')
def analysing():
	model=pickle.load(open("C:/Users/LENOVO/Desktop/project/modelhog.pickle","rb"))
	path1="C:/Users/LENOVO/Desktop/project/static/frame re2 sec.jpg"
ia.seed(1)

depth = np.linspace(0, 50, 128).astype(np.float32)  
depth = np.tile(depth.reshape(1, 128), (128, 1))    

depth[64-2:64+2, 16:128-16] = 0.75 * 50.0  
depth[16:128-16, 64-2:64+2] = 1.0 * 50.0   

# Convert our numpy array depth map to a heatmap object.
depth = HeatmapsOnImage(depth, shape=image.shape, min_value=0.0, max_value=50.0)


depth = depth.avg_pool(2)

# Define our augmentation pipeline.
seq = iaa.Sequential([
    iaa.Dropout([0.05, 0.2]),      
    iaa.Sharpen((0.0, 1.0)),       
    iaa.Affine(rotate=(-45, 45)),  
    iaa.ElasticTransformation(alpha=50, sigma=5)  
], random_order=True)

# Augment images and heatmaps.
images_aug = []
heatmaps_aug = []
for _ in range(5):
    images_aug_i, heatmaps_aug_i = seq(image=image, heatmaps=depth)
    images_aug.append(images_aug_i)
    heatmaps_aug.append(heatmaps_aug_i)

cells = []
for image_aug, heatmap_aug in zip(images_aug, heatmaps_aug):
    cells.append(image)                                                    # column 1
    cells.append(image_aug)                                                # column 2
    cells.append(heatmap_aug.draw_on_image(image_aug)[0])                  # column 3
    cells.append(heatmap_aug.draw(size=image_aug.shape[:2])[0])            # column 4
    cells.append(heatmap_aug.draw(size=image_aug.shape[:2], cmap=None)[0]) # column 5

# Convert cells to grid image and save.
grid_image = ia.draw_grid(cells, cols=5)
imageio.imwrite('"C:/Users/LENOVO/Desktop/project/static/frame re2 sec.jpg"', grid_image)
	return render_template("analyse.html")



	
@app.route('/out')
def outs():
	return render_template("output.html")

if __name__ == '__main__':
	app.run(debug=True)
