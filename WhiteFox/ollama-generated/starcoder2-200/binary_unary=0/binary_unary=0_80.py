
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor 
        v2  = v1 + other    # Add another tensor to the output of the convolution
        v3  = torch.relu(v2) # Apply the ReLU activation function to the result
        return v3


# Initializing the model and setting the seed for reproducible results
m = Model()
torch.manual_seed(0)


# Inputs to the model (x1 is a 4-D input tensor of size 8 x 3 x 64 x 64)
x1 = torch.randn(1, 3, 64, 64)
other = 0.5 * torch.ones(v1.shape[0], v1.shape[2] // 2 + v1.shape[3] % 2 - 1, \
                          v1.shape[-1], device=x1.device, dtype=x1.dtype)


