
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.dim = dim
 
    def forward(self, x1, x2):
        t1  = torch.mm(x1, x2) # Matrix multiplication of two input tensors
        t2 = torch.cat([t1, t1, *torch.ones((3-len(x1), )), t1])
        return t2

