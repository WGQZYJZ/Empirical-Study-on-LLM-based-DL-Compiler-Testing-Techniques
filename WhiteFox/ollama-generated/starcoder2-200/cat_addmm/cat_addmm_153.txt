
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.cat([x1], dim)
 
        return v2
 
# Initializing the model
m  = Model()


# Inputs to the model