
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.relu(x1)
        return 2 * v

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(4)
__output__  = m(x1)
 

