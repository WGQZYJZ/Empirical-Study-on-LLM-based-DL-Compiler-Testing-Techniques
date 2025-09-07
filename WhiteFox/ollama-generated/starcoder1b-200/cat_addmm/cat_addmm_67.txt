
class Model(torch.nn.Module):
    def __init__(self, input_tensor=None):
        super().__init__()
        self.input = torch.zeros(1, 3, 4, 5)
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
        v = self.conv(x)
        return self.input + v


# Initializing the model
m = Model()
# Inputs to the model
input_tensor = torch.randn(1, 3, 4, 5)
