class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self):
       return torch.full([2, 5], 3) # Create a tensor filled with the scalar value 1 and convert its elements to the data type `torch.float64` using `torch.double` as the argument for the function


# Initializing the model
m = Model()
__output__  = m()

