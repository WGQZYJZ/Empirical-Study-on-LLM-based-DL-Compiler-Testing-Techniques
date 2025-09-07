
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None): # Input 2
        v = torch.mm(x1, inp) # Matrix multiplication
        return v

