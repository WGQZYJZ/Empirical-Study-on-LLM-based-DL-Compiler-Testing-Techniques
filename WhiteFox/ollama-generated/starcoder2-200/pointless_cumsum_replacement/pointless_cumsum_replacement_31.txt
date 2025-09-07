
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        t1 = torch.full([arg1, arg2], 1)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)


# Initializing the model
m  = Model() 

 # Input to the model