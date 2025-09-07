
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8, 16)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1, inp):
        v1 = self.linear1(x1)
        v2 = self.relu(v1)
        return torch.mm(inp, v2)


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.randn(8)
