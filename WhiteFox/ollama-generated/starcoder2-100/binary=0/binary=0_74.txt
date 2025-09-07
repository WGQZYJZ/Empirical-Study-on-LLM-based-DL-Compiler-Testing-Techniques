
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        v2 = v1 + kwargs['other'] # 'other' is a keyword argument to the add operation. It is not an output of the convolution
        return v2

# Initializing the model with different keyword arguments. The model should be different from the previous one. 
other = torch.randn(3,8)
m = Model()
