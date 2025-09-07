
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1) + self.other  # Add another tensor to the output of the convolution and then assign it as the keyword argument to the addition operation
        return v1


# Initializing the model
m = Model(torch.randn(1, 3, 64, 64))


