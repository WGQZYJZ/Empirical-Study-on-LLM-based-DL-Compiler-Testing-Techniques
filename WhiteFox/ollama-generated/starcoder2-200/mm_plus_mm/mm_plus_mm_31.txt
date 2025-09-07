
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x3) 
        v2 = torch.mm(x4, x2) 
        return 10 + v1+v2
        
# Initializing the model