
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other # Note the addition operation: v1 is an output of a convolution and `other` represents another tensor to be added
        return v2

# Initializing the model
m = Model()

