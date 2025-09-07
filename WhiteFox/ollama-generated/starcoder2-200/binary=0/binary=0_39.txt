
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, other: torch.Tensor):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 + other # Add another tensor to the output of the convolution. The keyword argument is passed as "other" in this operation.
        return v2

# Initializing the model
m = Model()

