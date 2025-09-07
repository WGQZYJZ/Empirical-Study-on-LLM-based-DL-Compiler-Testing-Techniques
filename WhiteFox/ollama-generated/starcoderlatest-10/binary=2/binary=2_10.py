
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2


# Initializing the model and setting 'other' to a tensor of the same shape as the output of the convolution (i.e., 'other' is actually a constant tensor).
m = Model(torch.ones_like(output))

