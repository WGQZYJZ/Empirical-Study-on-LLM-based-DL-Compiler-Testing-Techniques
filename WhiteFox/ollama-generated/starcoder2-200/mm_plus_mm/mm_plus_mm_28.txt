
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2):
        v1  = torch.mm(x1, y2) 
        v4  = torch.mm(v1, y3) 
        return v4


# Initializing the model with three inputs and two outputs
m  = Model()

 # Inputs to the model