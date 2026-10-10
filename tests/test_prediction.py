{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c162387-4962-4de3-b5df-38276b769b84",
   "metadata": {},
   "outputs": [],
   "source": [
    "Test Cases Used in Fake Currency Detection Using Deep Learning\n",
    "In the Fake Currency Detection using Deep Learning project, test cases are used to check whether the trained model can correctly identify a currency note as Genuine or Fake by analyzing its image.\n",
    "1. Test Case Table\n",
    "Test Case ID\tTest Scenario\tInput\tExpected Result\n",
    "TC01\tGenuine currency note\tImage of a genuine note\tGenuine\n",
    "TC02\tFake currency note\tImage of a counterfeit note\tFake\n",
    "TC03\tClear currency image\tHigh-quality note image\tCorrect prediction\n",
    "TC04\tBlurred currency image\tBlurred note image\tPrediction or low confidence\n",
    "TC05\tRotated currency image\tRotated note image\tCorrect prediction if within model capability\n",
    "TC06\tDifferent lighting\tDark or bright image\tPrediction may vary\n",
    "TC07\tUnsupported image format\tText file or invalid image\tError message\n",
    "TC08\tNo image uploaded\tEmpty input\tPlease upload an image\n",
    "TC09\tUnseen currency image\tImage not used during training\tModel prediction\n",
    "TC10\tIncorrect image dimensions\tImage of a different size\tImage resized before prediction\n",
    "2. Sample Python Code for Testing\n",
    "The following code assumes you have already trained and saved your deep learning model and that you are using a binary classification model.\n",
    "import tensorflow as tfimport numpy as npfrom tensorflow.keras.utils import load_img, img_to_array# Load the trained modelmodel = tf.keras.models.load_model(\"fake_currency_model.keras\")def predict_currency(image_path):    try:        # Load and resize the image        img = load_img(image_path, target_size=(224, 224))        # Convert image to array        img_array = img_to_array(img) / 255.0        # Add batch dimension        img_array = np.expand_dims(img_array, axis=0)        # Predict        prediction = model.predict(img_array, verbose=0)        # For a sigmoid output: 0 = Fake, 1 = Genuine        score = float(np.squeeze(prediction))        if score >= 0.5:\n",
    "\n",
    "\n",
    "\n",
    "Important: Change the model filename, image dimensions, and class labels to match your project. The code assumes a sigmoid output with fake encoded as 0 and genuine as 1; your model may use a different encoding. A prediction alone does not establish whether a banknote is genuine.\n",
    "3. Performance Evaluation Test Cases\n",
    "After testing, evaluate your model using these metrics:\n",
    "- Accuracy: Percentage of correct predictions.\n",
    "- Precision: How many notes predicted as fake were actually fake.\n",
    "- Recall: How many fake notes were correctly detected.\n",
    "- F1-score: Balance between precision and recall.\n",
    "- Confusion matrix: Shows correct and incorrect predictions for both classes.\n",
    "4. Conclusion\n",
    "The test cases help verify the accuracy, reliability, and robustness of the fake currency detection system. Testing should use separate genuine and counterfeit images that were not included in the training dataset. Results should be recorded for each test case, and the model should be improved if it makes incorrect predictions."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b41ee277-5626-45ba-9344-be1eb2c6fea6",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import numpy as np\n",
    "import tensorflow as tf\n",
    "from tensorflow.keras.utils import load_img, img_to_array\n",
    "\n",
    "model_path = \"fake_currency_model.keras\"\n",
    "\n",
    "if os.path.exists(model_path):\n",
    "    model = tf.keras.models.load_model(model_path)\n",
    "    print(\"Model loaded successfully!\")\n",
    "\n",
    "    def predict_currency(image_path):\n",
    "        try:\n",
    "            if not os.path.exists(image_path):\n",
    "                print(\"Image file not found:\", image_path)\n",
    "                return\n",
    "\n",
    "            img = load_img(image_path, target_size=(224, 224))\n",
    "            img_array = img_to_array(img) / 255.0\n",
    "            img_array = np.expand_dims(img_array, axis=0)\n",
    "\n",
    "            prediction = model.predict(img_array, verbose=0)\n",
    "            score = float(np.squeeze(prediction))\n",
    "\n",
    "            if score >= 0.5:\n",
    "                print(\"Prediction: Genuine Currency\")\n",
    "            else:\n",
    "                print(\"Prediction: Fake Currency\")\n",
    "\n",
    "            print(\"Model score:\", round(score, 4))\n",
    "\n",
    "        except Exception as e:\n",
    "            print(\"Error:\", type(e).__name__, str(e))\n",
    "\n",
    "    predict_currency(\"test_currency.jpg\")\n",
    "\n",
    "else:\n",
    "    print(\"Model file not found:\", model_path)\n",
    "    print(\"Check the filename of your saved model.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9c756ce-b3f6-47f3-97c3-9b571954905b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "340e18bc-c3ec-4f2d-bfa7-07e636c0c951",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "576a90f3-bbe1-418a-b1e7-329464addaf1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4854002c-666e-42a8-bd6f-510cd2ccbddc",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "34c9368b-6e8b-460e-8dd7-e20b7711222d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0839c81c-3874-4e2b-900b-784358c71dbd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b95fdec5-7148-4fee-831d-6a94ce5f338f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
