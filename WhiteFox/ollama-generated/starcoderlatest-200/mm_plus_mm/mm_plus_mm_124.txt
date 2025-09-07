
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7, stride=2, padding=3)
        self.conv2 = torch.nn.Conv2d(64, 128, 5, stride=2, padding=2)
 
    def forward(self, x1):
        v1 = torch.mm(x1, x1) # Matrix multiplication between input and itself.
        v2 = self.conv1(x1)   # First convolution layer with output of size (batch_size, 64, 62, 62).
        v3 = self.conv2(v2)   # Second convolution layer with output of size (batch_size, 128, 26, 26).
        