
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, [64, 32], dim=0) # Split the input tensor along dimension 0 and return a list of three tensors.
        v5 = torch.cat([v2[0], v2[1]], dim=0) # Concatenate the first two tensors in the list v2 and return an output tensor.
 
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(64, 3, 64, 64)
