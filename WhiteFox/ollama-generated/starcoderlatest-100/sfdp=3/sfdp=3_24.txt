
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(10, 32)
        self.linear2 = torch.nn.Linear(32, 16)
        self.linear3 = torch.nn.Linear(16, 8)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = self.linear2(v1)
        v3 = self.linear3(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 8, 64, 64)
