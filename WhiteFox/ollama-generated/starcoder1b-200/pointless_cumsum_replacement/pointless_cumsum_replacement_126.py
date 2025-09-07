
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1 = torch.full([x1.shape[0], x1.shape[1]], 1, dtype=x1.dtype, layout=x1.layout, device=x1.device, pin_memory=x1.pin_memory)  # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        t2 = convert_element_type(t1, x1.dtype)  # Convert the elements of the tensor to the specified dtype
        t3 = torch.cumsum(t2, 1)  # Compute the cumulative sum of the elements of the tensor along dimension 1
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(2, 8, 64, 64)
__output__  = m(x1)

