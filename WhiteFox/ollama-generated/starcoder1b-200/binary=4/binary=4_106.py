
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 64)
        self.relu1  = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(64, 32)
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = self.relu1(v1)
        v3 = self.linear2(v2)
        return v3 + other


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, dtype=torch.float32, requires_grad=True)
