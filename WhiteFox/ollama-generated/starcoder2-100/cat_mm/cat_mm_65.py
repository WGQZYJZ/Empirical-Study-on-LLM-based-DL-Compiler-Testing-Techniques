
class Model(torch.nn.Module):
    def __init__(self, dim=3):
        super().__init__()
 
        self.dim = dim
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x1[1]) # Matrix multiplication of two input tensors

        v2  = []
        
        for i in range(self.dim + 1)
            t = v1 * 5
            v2 += [t]
            
        return torch.cat([v1, v1], dim=0), self._output__ = m((x1, x2))