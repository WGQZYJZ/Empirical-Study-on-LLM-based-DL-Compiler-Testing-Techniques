
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 256)
 
    def forward(self, x):
        v = self.linear(x)
        v = torch.relu(v - 0.5) # ReLU(t - 0.5) = t
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 2, 100)
