import cv2

test = cv2.imread("binary (blue-50-0).jpg")
correct = cv2.imread("accuracy (blue-50-0).jpg")

matches = 0

for i in range(len(test)):
    for j in range(len(test[i])):
        if test[i][j][0] == correct[i][j][0]:
            matches += 1

print(f"Accuracy: {matches / 2073600:%}")
