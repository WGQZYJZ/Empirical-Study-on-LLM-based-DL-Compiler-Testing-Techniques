
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v = torch.nn.functional.conv3d(x1)  # X1 is a 5D input tensor with 3D spatial shape and a 1D channel dimension
      bn = torch.nn.BatchNorm3d(4)         # BatchNorm3d uses the same 3D spatial shape as Conv3d
      output = bn(v)                       # The BatchNorm3d layer is tracking running statistics

      return output

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2, 4, 5, 8, 9)       
__output__  = m(x1)