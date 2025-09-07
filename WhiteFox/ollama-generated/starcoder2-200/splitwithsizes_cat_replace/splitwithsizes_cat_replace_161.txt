
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.split(x1, 256)
 

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(4096, 3, 8, 8)
x2_indices = [int(torch.floor(i / 2)) for i in range(len(x1))]  # Generates a list of indices to be used as argument to torch.split for the splitting operation.
x2 = x1[tuple(x2_indices)]


# Initializing the model
m = Model()
 
