
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2  = torch.rand(64) * self.__output__.shape[-3]
        v5  = torch.erf(v2 + torch.max(torch.ones_like(x1), 0))
        v7  = v5 + 1
        v8  = x1 * v7
        return v8
