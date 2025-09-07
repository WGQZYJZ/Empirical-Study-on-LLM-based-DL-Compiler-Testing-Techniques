
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.cat([x3], dim=1) # Concatenate the first concatenated tensor and the sliced tensor along dimension 1
        v1 = torch.cat([v2], dim=0) # Concatenate the concatenated tensors along dimension 0
        return v1
 
# Initializing the model
m = Model()


# Inputs to the model
x1, x3  = torch.randn(1, 487956143982499098), torch.randn(1, 3) # Creating two tensors
__output__  = m(x1, x3)

