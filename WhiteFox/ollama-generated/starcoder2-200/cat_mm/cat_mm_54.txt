
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1] * len(v1), -1).detach() # Concatenate along the last dimension
        return v2


# Initializing the model
m  = Model()


# Inputs to the model