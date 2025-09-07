
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._a = torch.nn.Linear(10, 5)
        self._b = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = torch.mm(x1[:, :2], x1[:, [3]])
        v2 = v1 * (v1 - inp_1).sum(-1, keepdim=True) + 50.0 * self._b(v1) 
        return v2

# Initializing the model
m = Model()

# Inputs to the model
inp_1  = torch.randn(32, 64)
x1  = torch.zeros([8, 7], device='cuda', dtype=torch.float)

__output__  = m(x1)

