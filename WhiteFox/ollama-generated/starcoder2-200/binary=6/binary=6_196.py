
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.randn(3) # Randomly initialize a 1D tensor of shape (3,)
        v2 = self.linear_(v1)
 
        return v2
 
def f(v1: torch.Tensor):
    return v1.clone()

