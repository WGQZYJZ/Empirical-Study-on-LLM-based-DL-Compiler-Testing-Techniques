
class Model(torch.nn.Module):
    def __init__(self, num_layers: int, dim_in: int, dim_out: int, dilation: int = 1):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(dim_in, dim_out, kernel_size=3, stride=1, padding=dilation * (dim_in - 1) / 2, dilation=dilation, bias=True)
 
    def forward(self, x):
        v1 = self.conv1(x) # Convolve the input with a filter tensor
        v2 = torch.cat([v1], dim=1) # Concatenate the result along channel dimension (channel last)
        return v2
 
# Initializing the model and inputs to the model
m = Model(num_layers, 3, 8, dilation=2)
x = torch.randn(1, 3, 64, 64)
