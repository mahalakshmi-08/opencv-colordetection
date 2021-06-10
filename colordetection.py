import cv2
import pandas as pd

# image address
img_path = r"C:\Users\HP PC\Desktop\python open image\images\pic1.jpg"
img = cv2.imread(img_path)

# indexes in csv file
index = ["color", "color_name", "hex", "R", "G", "B"]

# to read csv file
csv = pd.read_csv(r'C:\Users\HP PC\Desktop\python open image\images\colors.csv', names=index, header=None)

# to get color name from csv file
def getColorName(R, G, B):
    minimum = 1000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if (d < minimum):
            minimum = d
            color_name = csv.loc[i, "color_name"]
    return color_name

clicked = False
r = g = b = xpos = ypos = 0

# double click to find the color
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('color detection')
cv2.setMouseCallback('color detection', draw_function)
while (1):

    cv2.imshow("color detection", img)
    # to display the colors as r,g,b
    if (clicked):
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        color_name = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, color_name, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        #to display light colors
        if (r + g + b >= 600):
            cv2.putText(img, color_name, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # to exit press esc
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
