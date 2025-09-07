
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        # Add a tensor or scalar 0.5 from v2 to output of conv()
        v3  = torch.zeros_like(v1[:, :, 8, :]) # Zeroing out 1/2 of the tensor  (output channel size=4, kernel size=3, stride=1)
        v4  = v1 + v3
 
        # Add a scalar to the result from convolution
        v5  = torch.zeros_like(v4[:, :, :8, :]) # Zeroing out 1/2 of the tensor (output channel size=8, kernel size=3, stride=1)
        v6  = v4 + v5 + 0.7
 
        # Add a scalar to the result from ReLU activation function 
        v7  = torch.zeros_like(v4[:, :, :7, :]) # Zeroing out 1/2 of the tensor (output channel size=8, kernel size=3, stride=1)
        v8  = relu(v6 + v7 + 0.5)
 
        return v8


# Initializing the model
m = Model()
