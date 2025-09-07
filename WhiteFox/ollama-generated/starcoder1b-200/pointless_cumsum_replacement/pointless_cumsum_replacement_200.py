
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input_tensor = ...
        self.conv    = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self):
        v1   = self.conv(self.input_tensor)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v2   = torch.full([self.input_tensor.size()[1]], 1., dtype=v1.dtype, layout=v1.layout, device=v1.device, pin_memory=False)  # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        v3   = torch.cumsum(v2, dim=1)          # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = ...  # input_tensor
