
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, [1, 2], dim=3) # Split along third dimension
        v3 = torch.cat([v2[0], v2[1]], dim=3) # Concatenate the tensors along the third dimension
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8, 64, 192)
