
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0 = torch.randn(128)
        v1  = self.conv(x1) 
        v2 = linear(v1, other=v0) # Apply a linear transformation to the output of the pointwise convolution and add another tensor "other"
        return v2
