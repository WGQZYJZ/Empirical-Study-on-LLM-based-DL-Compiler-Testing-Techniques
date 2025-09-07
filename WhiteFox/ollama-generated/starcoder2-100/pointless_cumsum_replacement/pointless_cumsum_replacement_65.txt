
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2, dtype=None, layout=None, device=None):
        t1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device) # Create a tensor filled with the scalar value 1 with the specified dtype, layout, and device
        t3  = convert_element_type(t1, dtype) # Convert the elements of the tensor to the specified dtype
        return torch.cumsum(t3, dim=1), t2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randint(0, 5,(4))
x2 = torch.randint(0, 10,(3,))
 
 __output__  = m(x1[None,...], x2[None,...])
