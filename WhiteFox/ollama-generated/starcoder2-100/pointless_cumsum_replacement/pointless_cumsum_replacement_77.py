
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        t1 = torch.full([32, 4], 1., device=device) # Create a tensor filled with the scalar value 1.0
        t2 = t1 / float_value # Divide the elements of the created tensor by 5.0
        t3 = convert_element_type(t2, torch.int64) # Convert the elements of the created tensor to dtype int64
        return t3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(10, 32, 4)
__output__  = m(x1) 
