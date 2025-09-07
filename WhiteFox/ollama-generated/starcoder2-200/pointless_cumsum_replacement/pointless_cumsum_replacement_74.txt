
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2): 
        t1 = torch.full([arg1, arg2], 1, dtype=torch.float32) 
        t2 = torch.convert_element_type(t1, dtype=torch.float32)
        t3 = torch.cumsum(t2, dim=0) # Cumulative sum along dimension 1
        return t3


# Initializing the model
m = Model()

# Inputs to the model
arg1 = 5
arg2 = 6
__output__  = m(arg1, arg2)


