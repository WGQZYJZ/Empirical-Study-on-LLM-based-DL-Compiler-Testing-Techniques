
class Model(torch.nn.Module):
    def __init__(self, **kwarg):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + kwarg["other"] 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
kwarg = dict()
other = torch.randn(8, 3, 64, 64) # Tensor with the shape of (channel, width, height). In practice, the shape is often different from this one. But, it will be OK if the 0th channel dimension is the same as that in the previous example. 
x1 = torch.randn(1, 3, 64, 64) # Same as "x" in the previous example. But note: this tensor is not needed for generating the input tensor to the newly generated model.
kwarg["other"] = other

 