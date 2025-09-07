
class Model(torch.nn.Module):
    def __init__(self, other_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other_tensor):
        v1 = self.conv(x1) + other_tensor
        return v1


# Initializing the model
m = Model()
other  = torch.randn(3)  # A tensor that will be added to the output of the convolution
