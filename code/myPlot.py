import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json


with open("./log3",'r') as f:
    records = json.load(f)

epochs = []
main_loss = []
main_accuracy = []
validation_main_loss = []
validation_main_accuracy = []
for i in records:
    epochs.append(i["epoch"])
    main_loss.append(i["main/loss"])
    main_accuracy.append(i["main/accuracy"])
    validation_main_loss.append(i["validation/main/loss"])
    validation_main_accuracy.append(i["validation/main/accuracy"])

epochs = np.array(epochs)
main_loss = np.array(main_loss)
main_accuracy = np.array(main_accuracy)
validation_main_loss = np.array(validation_main_loss)
validation_main_accuracy = np.array(validation_main_accuracy)
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
