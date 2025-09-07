
class Model(torch.nn.Module):
    def __init__(self, n, m):
        super().__init__()
 
        self._weights = torch.nn.ParameterList([
            torch.nn.Parameter(
                torch.Tensor([[3] * n]).expand([-1, 3])) 
            for i in range(m) 
        ])
 
    def forward(self, x):
        v0 = []
        for w in self._weights:
            v0.append(torch.mm(x, w))
        v0 = torch.cat(v0, dim=2)
        return v0


# Initializing the model with the following parameters
m  = Model(30, 15) # m(x).size() == (64, 810, 90)

