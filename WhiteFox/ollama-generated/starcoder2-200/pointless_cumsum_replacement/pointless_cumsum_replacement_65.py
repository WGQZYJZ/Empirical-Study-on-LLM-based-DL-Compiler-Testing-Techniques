
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = torch.full([arg1, arg2], 1, dtype='torch.float64', device=device_arg1, pin_memory=False) # Create a tensor filled with the scalar value 1, with the specified dtype and device
        v2  = convert_element_type(v1, 'torch.double') # Convert the elements of the tensor to torch.double
        v3  = torch.cumsum(v2, 1)  # Compute the cumulative sum of the elements of the tensor along dimension `1`
        v4  = conv(x1)
        return v3 * v4


# Initializing model
m  = Model()
 
