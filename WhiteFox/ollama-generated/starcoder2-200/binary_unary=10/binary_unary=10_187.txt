
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 48)

    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = v1 + other 
        v3 = torch.relu(v2)
        return v3

# Initializing the model
m = Model()
other = torch.randn(100).view(-1, 48, 5)


# Inputs to the model