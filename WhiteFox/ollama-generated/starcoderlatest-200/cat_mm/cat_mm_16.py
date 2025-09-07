
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1)
        v2 = torch.cat([v1 for _ in range(3)])
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 5, 6, 7)
