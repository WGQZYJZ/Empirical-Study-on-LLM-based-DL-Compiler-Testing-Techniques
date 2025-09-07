
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x):
        v1  = torch.full([507, 238], 1, dtype=x[0].dtype) # Fill a tensor with the scalar value 1 of type torch.int64
        v2 = v1 + 68 # Add an arbitrary number to each element in the first dimension
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x0 = torch.randn(3, dtype=torch.double)
