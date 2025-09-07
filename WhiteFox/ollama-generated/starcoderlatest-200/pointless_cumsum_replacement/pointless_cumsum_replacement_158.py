
class Model(torch.nn.Module):
    def __init__(self, d, t):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, dtype):
        v1 = self.conv(x1).to(dtype)
        v2 = torch.cumsum(v1, 1)
        return v2


# Initializing the model with different types for arguments and input tensors of methods.
m = Model(torch.float32, torch.int64)
# Inputs to the model with the tensor dtype set as float32 and int64 respectively
x1 = torch.randn(1, 3, 64, 64).to(dtype)
