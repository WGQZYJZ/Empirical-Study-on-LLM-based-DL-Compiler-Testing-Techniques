
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 3)
 
    def forward(self, x):
        y = self.linear(x)
        return torch.sigmoid(y)


# Initializing the model
m = Model()


# Inputs to the model
input_tensor = torch.randn(10, 784)
