

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.mm
 
    def forward(self, x1, inp):
        v1  = self.mm(x1,inp)
        return v1 + inp


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2048, 512)
inp = torch.randn(2048,)


