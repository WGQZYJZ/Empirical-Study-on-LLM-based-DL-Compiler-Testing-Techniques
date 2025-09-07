
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self): 
        t1  = torch.full([2,3], 1, dtype=dtype)
        t2  = convert_element_type(t1, torch.float64)
        t3  = torch.cumsum(t2, 1) # cumsum(tensor, dim=0, dtype=None)
        return t3


# Initializing the model
m  = Model()

# Inputs to the model
