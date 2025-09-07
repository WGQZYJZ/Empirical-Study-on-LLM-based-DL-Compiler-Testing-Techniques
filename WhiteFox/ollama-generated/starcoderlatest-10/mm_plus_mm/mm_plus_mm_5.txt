
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(16, 24)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = torch.mm(x1, x1)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 16)
