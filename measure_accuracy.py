import cv2
from os import listdir
import numpy as np

accuracies = []
ball_accuracies = []

path = "/Users/akshatmehta/Downloads/benchmark/"
for file in listdir(path):

    test = cv2.imread(path + file)
    if "blue" in file[:30]:
        color = "blue"
    elif "red" in file[:30]:
        color = "red"
    else:
        continue

    correct = cv2.imread(f"/Users/akshatmehta/Downloads/binary/{color}_{file[file.index('benchmark_') + len('benchmark_'):]}")

    matches = 0
    ball_matches = 0
    ball_size = 0

    print(f"{color} in {file[file.index('benchmark_') + len('benchmark_'):]}")

    for i in range(len(test)):
        for j in range(len(test[i])):
            if test[i][j][0] == correct[i][j][0]:
                matches += 1
            if test[i][j][0] > 128:
                ball_size += 1
                if correct[i][j][0] > 128:
                    ball_matches += 1

    accuracies.append(matches / (correct.size / 3))
    ball_accuracies.append(ball_matches / ball_size)
    print(f"Total Accuracy: {accuracies[-1]:%}")
    print(f"Ball Accuracy: {ball_accuracies[-1]:%}\n")
    # cv2.imshow(f"Accuracy: {accuracies[-1]:%}, Ball Accuracy: {ball_accuracies[-1]:%}", np.vstack((test, correct)))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

print(accuracies)
print(ball_accuracies)
print(sum(accuracies)/len(accuracies))
print(sum(ball_accuracies)/len(ball_accuracies))
