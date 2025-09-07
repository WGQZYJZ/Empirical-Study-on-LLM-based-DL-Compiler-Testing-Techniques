
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...) # conv2d, 3D convolution layer
        self.bn1   = torch.nn.BatchNorm2d(...) # batch_norm, XNOR normalization layer

    def forward(self, x1):
        x2 = self.conv1(x1) 
        