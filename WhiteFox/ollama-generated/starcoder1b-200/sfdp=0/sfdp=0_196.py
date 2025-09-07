
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(784, 256)
        self.linear2 = torch.nn.Linear(256, 10)
 
    def forward(self, x):
        h = F.relu(self.linear1(x))
        return self.linear2(h)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 784)
