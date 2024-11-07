import torch

class NeuralNet(torch.nn.Module):

    def __init__(self):
        super(NeuralNet, self).__init__()

        self.linear1 = torch.nn.Linear(1024, 200)
        self.activation = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(200, 5)
        self.softmax = torch.nn.Softmax()

    def forward(self, x):
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.softmax(x)
        return x