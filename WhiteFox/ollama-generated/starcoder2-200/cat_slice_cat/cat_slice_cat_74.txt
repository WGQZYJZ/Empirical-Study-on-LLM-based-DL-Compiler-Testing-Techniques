

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.cat([x1] * len(x1), dim=0)
        return v1[::2][:len(x1)]


# Initializing the model
m  = Model()

# Inputs to the model
x1 = [torch.randn(5, 3, 64, 64) for _ in range(78907)]
