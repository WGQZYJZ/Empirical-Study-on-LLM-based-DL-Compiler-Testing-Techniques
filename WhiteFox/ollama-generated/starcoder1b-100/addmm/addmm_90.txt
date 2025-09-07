
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        return torch.mm(x1, inp)


# Initializing the model
m = Model()
inp  = torch.randn(1, 4, 32, 32)
