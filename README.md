# AI-Generated Image Detection Study

This study leverages cutting-edge deep learning architectures to enhance the detection of AI-generated images.

## Directory Structure

### I. Data_Processes
Contains the notebooks and scripts used for data collection and cleaning.

**Files:**
1. **mine_images.py**: Uses the BeautifulSoup library to extract images of art from various websites.
2. **Data_Curation.ipynb**: Includes data cleaning procedures performed on the novel dataset.

### II. Model_Building
Contains the notebooks for all model architectures, their training process, and evaluation metrics.

**Files:**
1. **Custom_2Block.ipynb**: Contains the 2-block CNN designed from scratch.
2. **Custom_4Block.ipynb**: Contains the 4-block CNN designed from scratch.
3. **Custom_4Block_BN.ipynb**: Contains the 4-block CNN with batch normalization designed from scratch.
4. **ResNet_Base_Model.ipynb**: Contains the ResNet50 base model evaluation.
5. **VGG_Base_Model.ipynb**: Contains the VGG16 base model evaluation.
6. **EfficientNet_Base_Model.ipynb**: Contains the EfficientNetV2B0 base model evaluation.
7. **EN_Convolutional_Refinement.ipynb**: Transfer Learning on EfficientNet with a Convolutional Layer.
8. **EN_Fully_Connected.ipynb**: Transfer Learning on EfficientNet with a Fully Connected Layer.
9. **EN_Pooling_Concatenation.ipynb**: Transfer Learning on EfficientNet with the concatenation of Average and Max Pooling, with a Dropout Layer.
10. **EN_BatchNorm.ipynb**: Transfer Learning on EfficientNet with 2 Dense Layers and Batch Normalization.
11. **Optimal_Model.ipynb**: Transfer Learning on EfficientNet with the optimal architecture (including kernel, activation, and bias normalization).
12. **EN_Hyperparameter_Tuning**: Hyperparameter tuning on the optimal model.

**Note:** The project does not use any code not written by me.

## Data Files Used

1. **[AI Recognition Dataset](https://www.kaggle.com/datasets/superpotato9/dalle-recognition-dataset)**
    - Contains over 20,000 AI-generated and real images.

2. **[Museum Art Dataset](https://www.kaggle.com/datasets/thedownhill/art-images-drawings-painting-sculpture-engraving?select=musemart)**
    - Contains over 3000 images of real-life drawings and paintings.

3. **[Abstract Gallery Dataset](https://www.kaggle.com/datasets/bryanb/abstract-art-gallery?select=Abstract_gallery)**
    - Contains over 5000 images of abstract gallery art.

The novel curated dataset can be found here: [Novel Curated Dataset](https://drive.google.com/drive/folders/1ENb_rKLfl7QZ3xvb8wSzwQ0VzXYYIWhv?usp=drive_link)

## Information About Code

- A separate notebook was created for each model to run multiple training processes in parallel. This led to code redundancy in data extraction, loading, and augmentation.
- Section definitions, redundant code related comments, and training process explanations can be found in the `Model_Building/ResNet_Base_Model.ipynb` notebook.