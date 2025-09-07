
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1] * 3 + [v1], dim=2)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1000) # Number of inputs to the model is randomized.
x2 = torch.randn(1, 1000)
