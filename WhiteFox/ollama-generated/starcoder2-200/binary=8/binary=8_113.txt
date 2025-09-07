
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + torch.tensor(1.) # Any input tensor is accepted here as long as its size matches the shape of the output of the convolution and the type is `torch.float`
        return v2


# Initializing the model