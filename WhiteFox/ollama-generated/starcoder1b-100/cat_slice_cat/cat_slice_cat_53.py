
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        output = torch.cat([x1, x2], dim=1)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(3, 3, 64, 64)
x2  = torch.randn(3, 3, 64, 64)
