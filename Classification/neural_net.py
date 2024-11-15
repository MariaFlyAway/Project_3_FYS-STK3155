import torch

class NeuralNet(torch.nn.Module):

    def __init__(self, input_dim=1024, output_dim=5):
        super(NeuralNet, self).__init__()

        self.linear1 = torch.nn.Linear(input_dim, 200)
        self.activation = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(200, output_dim)
        self.softmax = torch.nn.Softmax(dim=1)

    def forward(self, x):
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.softmax(x)
        return x