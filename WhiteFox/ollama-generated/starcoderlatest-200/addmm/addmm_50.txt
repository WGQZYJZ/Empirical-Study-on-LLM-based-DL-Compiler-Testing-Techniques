
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        return v1 + inp

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.randn(8, 3, 64, 64)
