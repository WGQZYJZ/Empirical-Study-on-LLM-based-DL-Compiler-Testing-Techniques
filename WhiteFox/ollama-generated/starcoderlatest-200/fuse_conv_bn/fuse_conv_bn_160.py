
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)

    def forward(self, x):
        return self.conv(x)  # This pattern is the same as module API pattern


# Initializing the model
m = Model()
# Inputs to the model
input_tensor = torch.randn(1, 2, 4, 4)
