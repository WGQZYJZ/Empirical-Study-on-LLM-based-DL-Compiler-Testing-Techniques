
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1) + self.other_tensor  # Here is the problem
        return v1


# Initializing the model with a tensor and passing it as an argument to the constructor
m = Model()
x2 = torch.randn(1, 3, 64, 64)  # x2 is added to the output of a pointwise convolution
