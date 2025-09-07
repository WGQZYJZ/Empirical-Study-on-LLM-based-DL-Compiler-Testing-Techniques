
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg0: int=32768):
        t0 = torch.full([arg0], 1)
        t1 = convert_element_type(t0, torch.float)
        t2 = torch.cumsum(t1, 1)
        return t2

# Initializing the model
m = Model()

 # Inputs to the model
x0 = 32768
 
 