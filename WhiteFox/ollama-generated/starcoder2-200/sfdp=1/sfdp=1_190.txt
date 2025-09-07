
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(0.1)
 
        self.inv_scale_factor  = self._compute_inverse_scale()
 
    @staticmethod
    def _compute_inverse_scale():
        return math.sqrt(1024)
 
    def forward(self, x1):
        v1 = torch.matmul(x1, x1)
        return v1
 
 
m = Model()

