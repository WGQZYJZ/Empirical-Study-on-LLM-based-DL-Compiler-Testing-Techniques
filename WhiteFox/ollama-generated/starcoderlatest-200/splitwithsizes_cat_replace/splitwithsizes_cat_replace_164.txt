
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.split(x1, 2, dim=3) # Split tensor along dimension `dim` (assuming the model has been constructed in such a way as to allow splitting along this dimension).

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
