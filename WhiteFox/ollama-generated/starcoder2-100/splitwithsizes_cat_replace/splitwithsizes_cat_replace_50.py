
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2): 
        return torch.split(x1, [3]) + torch.split(x2, [4])[0]


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(5)
x2  = torch.randn(8)
