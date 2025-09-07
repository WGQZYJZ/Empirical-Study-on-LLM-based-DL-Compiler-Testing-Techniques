
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
      # Split the input tensor into four tensors along channel dimension (0th-axis of the tensor), and the first three tensors are used for convolutions, and the fourth tensor is not used in this optimization.
        split_tensors = torch.split(x1, [8 * 2], dim=0)
        
        v1 = self.conv(split_tensors[0])  # Use the first channel for pointwise convolution with kernel size 3 x 3
        v4 = self.conv(split_tensors[-1])  # Use the last channel for pointwise convolution with kernel size 3 x 3

        return torch.cat([v1, v4], dim=0)


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(8 * 2 + 5, 3, 64, 64)
