
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): # Input to the first BMM operation
        t2 = torch.bmm(x1.permute(0, 2, 1), x3)

        return t2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 4, 2) # A
x2 = torch.randn(2, 5, 3)  # B
x3 = torch.randn(2, 3, 7)   # C

 __output__  = m(x1)

 