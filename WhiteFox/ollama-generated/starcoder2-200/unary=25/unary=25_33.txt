
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.where(x1 > 0, x1, -2)
 
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(8)