

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.full([320, 784], 1) # Initialize the tensor to a specified value (default is zero). 
        v2  = v1 + torch.cumsum(v1, 1) # Apply cumulative sum to the tensor along dimension `1`
        return v2

# Initializing the model
m = Model()


# Inputs to the model