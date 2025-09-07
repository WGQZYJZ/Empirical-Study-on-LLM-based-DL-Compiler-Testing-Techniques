
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn(x1.shape) 
        v3  = torch.normal.normal_(v2, mean=0., std=1.) # Apply a normal distribution to another tensor 
__output__  = torch.sum(x1 * v3)
 