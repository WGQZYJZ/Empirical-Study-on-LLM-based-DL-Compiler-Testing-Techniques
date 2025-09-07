
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        t1  = torch.full([x1.size()], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)  # Create a tensor filled with the scalar value 1, with the specified dtype, layout, and device
        t2  = convert_element_type(t1, dtype)  # Convert the elements of the tensor to the specified dtype
        t3  = torch.cumsum(t2, 1)  # Compute the cumulative sum of the elements of the tensor along dimension 1
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
