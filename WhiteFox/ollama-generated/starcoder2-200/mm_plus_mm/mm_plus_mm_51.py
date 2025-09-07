
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):
        v0  = torch.mm(x1, x2) 
        v1  = torch.mm(v0 , x3) 
        v2  = torch.mm(v1 + v0, x4) # This is a model that performs three matrix multiplications with different input matrices.
        return v2


# Initializing the model
m  = Model()
 
