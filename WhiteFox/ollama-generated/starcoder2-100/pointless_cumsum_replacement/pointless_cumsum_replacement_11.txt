
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
        torch.full([32, 32], 1).type(dtype=torch.double)  # Create a tensor filled with the scalar value 1, with the dtype `torch.double`


# Initializing the model
m = Model()

# Inputs to the model
