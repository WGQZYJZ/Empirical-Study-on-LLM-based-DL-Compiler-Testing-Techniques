
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.Linear(4, 16)
 
    def forward(self, x1, y1, z1, k1):
        v2  = self.mm(x1 + y1 + z1 - k1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model 
x1  = torch.randn(8, 4)
y1  = torch.randn(9, 3)
z1  = torch.randn(7, 5)
k1  = torch.tensor([2])
__output__  = m(x1, y1, z1, k1)

