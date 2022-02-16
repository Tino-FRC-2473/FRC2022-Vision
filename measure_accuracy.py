import cv2
from os import listdir
import numpy as np

path = "/Users/akshatmehta/Downloads/benchmark/"
for i in listdir(path):

    test = cv2.imread(path + i)
    if "blue" in i[:30]:
        color = "blue"
    elif "red" in i[:30]:
        color = "red"
    else:
        continue
    correct = cv2.imread(f"/Users/akshatmehta/Downloads/binary/{color}_{i[i.index('benchmark_') + len('benchmark_'):]}")

    matches = 0

    for i in range(len(test)):
        for j in range(len(test[i])):
            if test[i][j][0] == correct[i][j][0]:
                matches += 1

    accuracy = matches / (correct.size / 3)
    print(f"Accuracy: {accuracy:%}")
    # if accuracy < 0.95:
    #     cv2.imshow(f"Accuracy: {accuracy:%}", np.vstack((test, correct)))
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()
