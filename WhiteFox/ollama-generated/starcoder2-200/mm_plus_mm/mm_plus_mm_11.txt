
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mm(x1[0], x1[1]) 
        v2 = torch.mm(x1[3][0], x1[4][1]) 
        v3 = v1 + v2 # Matrix multiplication between input 1 and input 2 and add them together
        return v3


# Initializing the model