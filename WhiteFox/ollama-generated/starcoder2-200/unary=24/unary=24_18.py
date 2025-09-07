
class Model(torch.nn.Module):
    def __init__(self, negative_slope):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
 
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 > 0
        v4 = torch.where(v2, v1, v1 * self.negative_slope) # Where the output of the convolution is greater than 0, multiply it by negative slope; otherwise multiply it by itself.
        return v4


# Initializing the model