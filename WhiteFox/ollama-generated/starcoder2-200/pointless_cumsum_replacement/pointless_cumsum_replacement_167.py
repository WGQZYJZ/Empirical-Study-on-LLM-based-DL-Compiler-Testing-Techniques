
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self): 
        v1  = torch.full([5, 3], 1)
        return torch.cumsum(v1, 1)

 # Initializing the model
 m  = Model()
 
# Inputs to the model