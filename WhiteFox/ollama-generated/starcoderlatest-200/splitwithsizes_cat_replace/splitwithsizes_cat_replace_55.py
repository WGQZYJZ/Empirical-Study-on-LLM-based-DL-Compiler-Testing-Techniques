
class Model(torch.nn.Module):
    def __init__(self, dimension=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(16, 3, (3, 3), stride=(2, 2), padding=(1, 1))
        self.pooling_layer = torch.nn.AdaptiveAvgPool2d((40, 40))
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.pooling_layer(v1)
        return v2


# Inputs to the model
x1 = torch.randn(16, 16, 80, 45)
