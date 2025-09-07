
class Model(torch.nn.Module):
    def __init__(self, conv_filter_size=16):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, conv_filter_size, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v6


# Initializing the model
m = Model()
other = torch.randn(conv_filter_size, 3, 64, 64)
