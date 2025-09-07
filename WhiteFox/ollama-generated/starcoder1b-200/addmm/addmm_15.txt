
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2=None):
        if x2 == None:
            inp = torch.randn(1, 3)
        else:
            inp = x2
        v1 = torch.mm(x1, x2)
        return v1 + inp


# Initializing the model
m = Model()


# Inputs to the model
input1 = torch.randn(4, 5, 64, 64)
output = m(input1)


