

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(784, 32*360)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = v1 - 59.432
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()
 
# Inputs to the model
inputs = torch.randn(784)


# Valid PyTorch model
m(inputs).shape