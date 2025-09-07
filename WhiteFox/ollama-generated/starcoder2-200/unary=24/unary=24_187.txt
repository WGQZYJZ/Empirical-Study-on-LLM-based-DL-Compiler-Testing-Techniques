

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 > 0

        # If the output of the convolution is greater than or equal to 0, then multiply by negative_slope, otherwise, leave it unchanged.
        v3 = torch.where(v2, v1, v1*negative_slope )
        
        return v3