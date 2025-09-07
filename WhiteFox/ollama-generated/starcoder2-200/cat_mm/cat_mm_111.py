
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.Linear(16, 8)
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v2  = torch.cat([v1] * 3)
        return v2


# Initializing the model
m  = Model()

# Input tensors to the model
x1 = torch.randn(16, 8).double()
x2 = torch.randn(16, 4).double()
__output__  = m(x1, x2)


