
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = other + v1  # We add another tensor to the output of the convolution (v1 is used in this pattern)
        v5  = torch.relu(v4)
        return v5


# Initializing the model