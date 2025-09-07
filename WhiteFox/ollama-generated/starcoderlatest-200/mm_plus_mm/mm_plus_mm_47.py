
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 5)
        self.linear2 = torch.nn.Linear(5, 3)
 
    def forward(self, x1, x2, x3):
        v1 = self.linear1(x1)
        v2 = self.linear2(v1 + x2 + x3)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3072)
x2 = torch.randn(1, 5, 4096)
x3 = torch.randn(1, 3, 6144)
