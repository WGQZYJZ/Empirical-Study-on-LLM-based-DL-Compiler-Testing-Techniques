
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1):
        v1  = torch.mm(x1)
        return v2

 # Initializing the model