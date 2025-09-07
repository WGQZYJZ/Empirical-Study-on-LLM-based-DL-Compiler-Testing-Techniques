
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v = torch.mm(x1, inp)
        return v + inp

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
inp = torch.randn(3, 8, 64, 64)
