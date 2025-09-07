
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        t1 = torch.full([x1, x2], 1)
        t2 = convert_element_type(t1, dtype)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Inputs to the model
x1 = 2
x2 = 64
