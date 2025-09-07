
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.full([504327], 1., dtype=dtype, layout=layout)
        v1 = convert_element_type(v1, dtype)
        v1 = torch.cumsum(v1, 1)


# Initializing the model
m = Model()

# Inputs to the model
