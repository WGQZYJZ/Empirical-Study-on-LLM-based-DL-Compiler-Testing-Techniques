
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1)
 
    def forward(self, x): 
        v7 = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        return v7

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(2,3,64,64)
__output__  = m(x1)


## References
- [torch.nn.Conv2d](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html#torch.nn.Conv2d)