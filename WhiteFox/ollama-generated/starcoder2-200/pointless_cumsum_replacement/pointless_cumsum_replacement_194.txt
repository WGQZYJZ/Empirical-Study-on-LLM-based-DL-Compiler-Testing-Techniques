
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.full([32], 0, dtype=dtype)
        t1 = convert_element_type(t1, torch.double)
        t2 = torch.cumsum(t1, 1)
        return t2
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.ones([32], dtype=dtype)
 
