
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.linear(x1.permute(0, 2, 1), 3) 
        return v2


# Initializing the model
m = Model()



# Inputs to the model
x1  = torch.randn(5,4,786)
__output__  = m(x1)

