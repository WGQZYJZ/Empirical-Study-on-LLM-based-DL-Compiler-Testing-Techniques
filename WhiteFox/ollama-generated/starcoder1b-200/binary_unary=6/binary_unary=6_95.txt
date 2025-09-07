
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096, 128)
 
    def forward(self, x):
        v = F.relu(self.linear(x))
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 160, 160)
