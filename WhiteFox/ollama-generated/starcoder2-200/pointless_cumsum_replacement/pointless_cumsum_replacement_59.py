
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        v1 = torch.full([arg1, arg2], 1)
        v2 = convert_element_type(v1, dtype) 
        return torch.cumsum(v2, 1)


# Initializing the model
m = Model()

# Inputs to the model