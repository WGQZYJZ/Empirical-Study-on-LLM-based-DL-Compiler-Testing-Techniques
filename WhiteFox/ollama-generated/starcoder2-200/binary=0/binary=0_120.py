
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1  = self.conv(x1) 
        return v1 + other # The new part here

