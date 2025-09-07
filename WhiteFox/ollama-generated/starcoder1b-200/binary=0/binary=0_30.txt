
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = v1 + other  # Add the output of the convolution and the "other" tensor to form the final result
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
other = torch.randn(1, 8)
