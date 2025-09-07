
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*16, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = v1 + x2
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 16, 40)
x2 = torch.randn(32, 16, 8)
