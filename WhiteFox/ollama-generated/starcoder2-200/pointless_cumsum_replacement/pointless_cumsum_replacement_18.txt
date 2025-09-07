
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, arg1, arg2):
        v1  = torch.full([arg1, arg2], 1) 
        return convert_element_type(v1, dtype)

# Initializing the model
m  = Model()


# Inputs to the model