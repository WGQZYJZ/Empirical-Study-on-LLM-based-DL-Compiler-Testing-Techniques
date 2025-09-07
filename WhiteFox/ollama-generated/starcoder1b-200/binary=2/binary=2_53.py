
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1) - self.other  # Here we use different variables for each step of the subtraction to make the code readable
        return v1


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
v2 = Model(x1)
