
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        return torch.cat([x1 * x2, x1 * x2, 
                          ... , x1 * x2], dim=0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(4, 3, 5000, 6000)
x2 = torch.randn(4, 3, 800, 900)
