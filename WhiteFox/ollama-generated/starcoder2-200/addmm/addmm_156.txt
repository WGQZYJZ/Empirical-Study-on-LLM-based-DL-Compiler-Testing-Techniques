
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp):
        v1 = torch.mm(x1,inp)
        v2 = v1 + inp  # the result of the multiplication is added to 'inp' 
        return v2

# Initializing the model with different initializers
m = Model()


# Inputs to the model
inp = torch.randn(48, 63)

x1  = torch.rand(750, 39, dtype=torch.float)
