
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1: int, arg2 :int): 
        v1 = torch.full([arg1, arg2], 1)
        v2 = convert_element_type(v1, 'float') # Convert the elements of the tensor to the specified dtype
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()
 
 

# Inputs to the model