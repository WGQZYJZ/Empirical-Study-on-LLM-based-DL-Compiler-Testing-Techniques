
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x0, x1):
        t0 = torch.cat([x0, x1], dim=1) # Concatenate two input tensors along dimension 1
        t1 = t0[:, :size] # Slice the concatenated tensor along dimension 1
        t2 = self.conv(t1) # Apply pointwise convolution to the sliced tensor with a kernel size of 1
        return t2


# Initializing the model
m = Model(7453)

# Inputs to the model
x0 = torch.randn(1, 3, 64, 64) # A random input tensor for the first input tensor of the model
x1 = torch.randn(1, 3, 64, 64) # A random input tensor for the second input tensor of the model


__output__  = m(x0, x1)

