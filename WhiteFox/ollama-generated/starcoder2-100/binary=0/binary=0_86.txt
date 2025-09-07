
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1) + other # This is how the output of the convolution is added to "other" (i.e., a tensor that was passed as an argument during the call).
        return v1


# Initializing the model