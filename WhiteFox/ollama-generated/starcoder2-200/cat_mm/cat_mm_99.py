
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.cat([v1] * 5)
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(4096, 784)
x2 = torch.randn(3, 4096)

 __output__  = m(x1, x2)


# Description of requirements