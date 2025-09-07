
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 5)
 
    def forward(self, x1, y1):
        v1 = torch.mm(x1[:, None], y1[None])
        return torch.mm(v1, v1)

m = Model()

 # Inputs to the model
x1  = torch.randn(8092, 4)
y1  = torch.randn(5763, 4)
 
__output__  = m(x1, y1)

