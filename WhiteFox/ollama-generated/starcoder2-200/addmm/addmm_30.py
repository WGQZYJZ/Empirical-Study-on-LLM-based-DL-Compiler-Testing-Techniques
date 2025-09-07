
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inp = torch.randn((2,5))
 
    def forward(self, x1):
        v1  = torch.mm(x1, inp) # mm is Matrix multiplication
        return v1
