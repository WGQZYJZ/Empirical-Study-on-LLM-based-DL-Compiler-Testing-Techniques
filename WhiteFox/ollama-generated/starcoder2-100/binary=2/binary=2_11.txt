
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - other_tensor
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(1,3,64,64)
other_tensor = torch.randn(8, 8, 500, 500) # Tensor with shape (8, 8, 500, 500).
__output__   = m(x1)

# Description of requirements for the model input tensor
The input to the model should be a valid 4D torch.Tensor in `NCHW` format. The number of channels (N) should be 3. The channel size of each channel is 8. The height, width and batch sizes are 64.
 