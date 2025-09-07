
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(32768, 10)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + other # where `other` is some tensor of the same size and type as the output of `v1`
        return v2


# Initializing model
m = Model()

# Inputs to the model
other = torch.randn(4, 3)  # dummy tensor used in this example
x1 = torch.rand(4, 3, 64, 50).to('cuda')
__output__  = m(x1)

