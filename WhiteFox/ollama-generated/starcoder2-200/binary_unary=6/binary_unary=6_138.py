
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Applying  pointwise convolution to the input tensor (which is already 1D-channel)
        v2  = v1 - 487
        v3  = torch.relu(v2)
