
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        t1  = torch.full([arg1, arg2], 1, dtype=dtype, layout=layout, device=device) 
        t2  = convert_element_type(t1, dtype)  
        t3  = torch.cumsum(t2, 1)
        return t3

# Initializing the model
m  = Model()

# Inputs to the model
__args1__, __args2__  = [arg1, arg2]
__output__  = m(__args1__, __args2__)

