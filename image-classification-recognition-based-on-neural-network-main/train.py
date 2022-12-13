import torch
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

from model import *

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

train_data = torchvision.datasets.CIFAR10(root="venv/train_data",
                                          train=True,
                                          transform=torchvision.transforms.ToTensor(),
                                          download=True)
test_data = torchvision.datasets.CIFAR10(root="venv/test_data",
                                         train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)

train_data_size = len(train_data)
test_data_size = len(test_data)

train_dataloader = DataLoader(train_data, batch_size=64)
test_dataloader = DataLoader(test_data, batch_size=64)

nnp = NNP()
nnp.to(device)

loss_fn = nn.CrossEntropyLoss()
loss_fn.to(device)

optimizer = torch.optim.SGD(nnp.parameters(), lr = 0.01)

total_train_step = 0
total_test_step = 0
epoch = 100

writer = SummaryWriter("../logs_train")

for i in range(epoch):
    print("The {} time train.".format(i+1))
    nnp.train()
    for data in train_dataloader:
        imgs, targets = data
        imgs.to(device)
        targets.to(device)
        outputs = nnp(imgs)
        loss = loss_fn(outputs, targets)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_step += 1
        if total_train_step%50 == 0:
            print("Time of train: {}, Loss: {}".format(total_train_step, loss))
            writer.add_scalar("train_loss", loss.item(), total_train_step)

    nnp.eval()
    total_test_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_dataloader:
            imgs, targets = data
            imgs.to(device)
            targets.to(device)
            outputs = nnp(imgs)
            loss = loss_fn(outputs, targets)
            total_test_loss += loss.item()
            accuracy = (outputs.argmax(1) == targets).sum()
            total_accuracy += accuracy
        print("The loss on total data: {}".format(total_test_loss))
        print("The accuracy rate on the total data: {}".format(total_accuracy/test_data_size))
        writer.add_scalar("test_loss", total_test_loss, total_test_step)
        writer.add_scalar("test_accuracy", total_accuracy/test_data_size, total_test_step)
        total_test_step += 1
        torch.save(nnp, "nnp_{}.pth".format(i))
        print("The model has been saved.")
        total_train_step = 0

writer.close()