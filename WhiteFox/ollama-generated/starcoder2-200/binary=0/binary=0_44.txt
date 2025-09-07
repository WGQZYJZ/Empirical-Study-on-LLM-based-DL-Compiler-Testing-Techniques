
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + kwargs['other'] # Add the "other" tensor to the output of the convolution 
        return v2


# Initializing and running the model
m  = Model(**{'other': torch.randn(5, 4)})
x1 = torch.randn(1, 3, 64, 64)
