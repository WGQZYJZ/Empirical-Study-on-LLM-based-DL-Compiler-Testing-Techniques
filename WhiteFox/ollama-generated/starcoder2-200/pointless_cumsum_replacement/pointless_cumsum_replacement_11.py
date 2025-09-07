
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([4096,], -2.0785e-3)
        v1 = convert_element_type(v1, dtype=torch.float32) # Convert the elements of the tensor to `dtype`
        v1 = torch.cumsum(v1, 1)
        return v1
# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.zeros((4096,))

 __output__  = m (x1 )

