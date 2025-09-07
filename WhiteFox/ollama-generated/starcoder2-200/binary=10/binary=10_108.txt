
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.Linear()(x1) + torch.nn.Conv2d()(x1)  # linear + conv
        return v1


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(5, 3, 64, 64)
