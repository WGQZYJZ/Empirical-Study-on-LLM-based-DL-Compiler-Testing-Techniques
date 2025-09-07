
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.addmm(x1, mmat2, mmat1)  # A dummy matrix, the user should not use it.
        v1 = self.cat(v0)
 
        return v1
 
