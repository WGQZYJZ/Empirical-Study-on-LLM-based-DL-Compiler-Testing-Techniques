
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      v1 = torch.nn.functional.conv3d(x1, conv3d.weight) # Apply the 3D convolution to the input tensor.
      v2 = torch.nn.functional.batch_norm3d(v1, batch_norm3d.weight, batch_norm3d.bias, batch_norm3d.running_mean, batch_norm3d.running_var) # Apply the 3D batch normalization to the output of the convolution layer.
      return v2

m = Model()
x1 = torch.randn(4, 3, 50, 80, 90)
