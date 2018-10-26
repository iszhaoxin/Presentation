import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json, os
        
def plot_loss_and_accuracy(self):
    plt.ylim(ymax=1)
    plt.grid(color='k', linewidth=1,alpha=0.1)

    plt.plot(epochs, main_loss, label='main/loss')
    plt.plot(epochs, validation_main_loss, color='orange', label='validation/main/loss')
    plt.xlabel('epochs',size=12)
    plt.ylabel('loss',size=12)
    # plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.legend()
    # plt.show()

    fig2 = plt.figure()
    plt.plot(epochs, main_accuracy, label='main/accuracy')
    plt.plot(epochs, validation_main_accuracy, color='orange', label='validation/main/accuracy')
    plt.legend()
    plt.ylim(ymax=1)
    plt.xlabel('epochs',size=12)
    plt.ylabel('accuracy',size=12)
    plt.grid(True)
    fig2.savefig("14.png")
    plt.legend()
    # plt.show()

def read(fn):
    print(fn)
    with open(fn,'r') as f:
        records = json.load(f)

    epochs = []
    main_loss = []
    main_f1_score = []
    main_accuracy = []
    validation_main_loss = []
    validation_main_accuracy = []
    validation_main_f1_score = []
    for i in records:
        epochs.append(i["epoch"])
        main_loss.append(i["main/loss"])
        main_accuracy.append(i["main/accuracy"])
        validation_main_loss.append(i["validation/main/loss"])
        validation_main_accuracy.append(i["validation/main/accuracy"])
        main_f1_score.append(i["main/f1_score"])
        validation_main_f1_score.append(i["validation/main/f1_score"])
    epochs = np.array(epochs)
    main_loss = np.array(main_loss)
    main_accuracy = np.array(main_accuracy)
    main_f1_score = np.array(main_f1_score)
    validation_main_loss = np.array(validation_main_loss)
    validation_main_f1_score = np.array(validation_main_f1_score)
    validation_main_accuracy = np.array(validation_main_accuracy)
    print(max(validation_main_accuracy))
    print(max(validation_main_f1_score))
    return max(validation_main_f1_score), max(validation_main_accuracy)

def plot_array(array, y_label, savefn):
    plt.figure()
    plt.ylim(ymin=0, ymax=1)
    plt.grid(color='k', linewidth=1,alpha=0.1)
    xdata = np.array(range(0,len(array)))
    y1data = array
    title = savefn.split('.')[0]
    plt.title(title)
    plt.plot(xdata, y1data, color='orange', label=y_label)
    plt.xlabel('layers',size=12)
    plt.ylabel('value',size=12)
    # plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig(savefn)
    plt.legend()
    plt.close(0)

root = "/home/dreamer/files/presentations/IE_10_24/code/ShallowConcateS2/"
record_accuracy = np.zeros(9, dtype=float)
record_f1_score = np.zeros(9, dtype=float)
for directory in os.listdir(root):
    if os.path.isdir(root+directory):
        f1, accu = read(root+directory+'/log')
        print(int(directory))
        record_f1_score[int(directory)] = f1
        record_accuracy[int(directory)] = accu
plot_array(record_f1_score, y_label="f1_score", savefn="f1_score.png")
plot_array(record_accuracy, y_label="accuracy", savefn="accuracy.png")

