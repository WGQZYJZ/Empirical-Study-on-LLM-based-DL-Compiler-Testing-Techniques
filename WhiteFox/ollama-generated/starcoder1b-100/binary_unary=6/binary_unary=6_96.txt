
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 128, 4096)

    def forward(self, x):
        return relu(self.conv(x))


# Initializing the model
m = Model()

# Inputs to the model
x  = torch.randn(1, 3, 256, 256)
