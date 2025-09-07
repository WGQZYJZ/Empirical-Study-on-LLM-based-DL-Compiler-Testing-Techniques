

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + self._other_tensor()
        return v2

m = Model()

x = torch.randn(8, 32)
__output__  = m(x)

# Initializing the model and replacing one tensor in it with a randomly generated one
m = Model()
m.__other__.data  = torch.randn_like(m._other_.data)

