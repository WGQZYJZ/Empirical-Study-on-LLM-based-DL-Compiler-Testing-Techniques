
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, dim=0):
        # Concatenate along a specified dimension
        return torch.cat([x1, x2, ..., x2], dim)


# Initializing the model
m = Model()


