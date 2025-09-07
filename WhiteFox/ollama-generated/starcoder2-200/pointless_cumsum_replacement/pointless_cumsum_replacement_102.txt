
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, arg1): # arg1: int
        v1 = torch.full([arg1], 1) # Create a tensor filled with the scalar value 1.
        v2 = convert_element_type(v1, torch.double) # Convert the elements of the tensor to dtype double.
        v3 = torch.cumsum(v2, 0)
        return v3


# Initializing the model and passing in argument arg1
arg1 = 5
m  = Model()
__output__= m(arg1)
