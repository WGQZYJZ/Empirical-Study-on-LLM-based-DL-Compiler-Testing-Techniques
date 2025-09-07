
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp):
        v1 = torch.mm(x1, inp)
        v2 = v1 + inp 
        return v6

 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp = torch.randn(8, 3)
