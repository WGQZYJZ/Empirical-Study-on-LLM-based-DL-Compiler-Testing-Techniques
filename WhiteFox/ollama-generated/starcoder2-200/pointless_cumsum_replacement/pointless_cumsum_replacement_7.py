
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):

        return 5

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3)

__output__  = m(x1)

