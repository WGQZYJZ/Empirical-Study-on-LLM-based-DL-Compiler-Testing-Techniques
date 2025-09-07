
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.full([x1, x2], 1, dtype=torch.float32, layout='C') # Create a tensor filled with the scalar value 1, with the specified dtype, layout and device
        v2 = torch.cumsum(v1, 0) # Compute the cumulative sum of the elements of the tensor along dimension 0
        return v2


# Initializing the model
m = Model()


