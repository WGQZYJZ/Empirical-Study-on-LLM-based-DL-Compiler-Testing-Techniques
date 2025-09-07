
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        x_t = torch.cat([x1, x2, x1, x1], 0)
        return x_t

 # Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(2, 8, 64, 64)
