
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
 
        v2_other  = torch.nn.Parameter(torch.rand((3,8), dtype=torch.float64)) # A random Tensor
        v3  = v1 - v2_other # Subtract a Tensor or scalar "v2_other" from the output of the convolution
        v5  = self.relu(v3) # Apply ReLU to the result 
        return v5

    @staticmethod
    def relu(x):
      return torch.max(torch.tensor([0.], dtype=torch.float64), x + 1e-29)


# Initializing and running the model
m = Model()
output = m(x1)


