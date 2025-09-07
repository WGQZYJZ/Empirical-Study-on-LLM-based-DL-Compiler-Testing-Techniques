
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, a1, b1):
        v1  = torch.mm(x1,y1) 
        v2  = torch.mm(z1,a1)
        v3  = v1 + v2 # Addition of the results of two matrix multiplications
        return v3
# Initializing the model