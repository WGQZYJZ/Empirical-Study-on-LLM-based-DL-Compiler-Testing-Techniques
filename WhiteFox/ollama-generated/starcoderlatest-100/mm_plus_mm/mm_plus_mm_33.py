
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm1 = torch.nn.Linear(3, 2)
        self.mm2 = torch.nn.Linear(4, 3)
 
    def forward(self, x1, x2, x3, x4):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3) # batch size 1 with 3 channels
x2 = torch.randn(1, 4)
x3 = torch.randn(1, 6) # batch size 1 with 6 channels
x4 = torch.randn(1, 7)
