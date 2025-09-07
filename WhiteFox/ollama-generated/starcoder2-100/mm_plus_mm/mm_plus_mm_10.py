
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v3 = torch.mm(x1, x2) # Apply matrix multiplication to the inputs 
        v4  = torch.mm(x1, x2) # Apply another matrix multiplication to the inputs
        v5  = v3 + v4 # Add the outputs of the first two matrix multiplications together

# Initializing and running model:
m = Model()
