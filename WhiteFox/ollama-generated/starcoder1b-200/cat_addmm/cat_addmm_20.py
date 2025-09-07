
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(32, 8)
        self.fc2 = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        v1  = x1 + 0.5  # Add the input to a constant of value `0.5`
        v2  = torch.tanh(self.fc1(v1))
        v3  = self.fc2(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 32)
