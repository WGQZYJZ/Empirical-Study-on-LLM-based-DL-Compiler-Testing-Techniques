
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 1)

    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.sigmoid(v1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1024, 784) # The input tensor has a shape of (batch size, number of features). 
