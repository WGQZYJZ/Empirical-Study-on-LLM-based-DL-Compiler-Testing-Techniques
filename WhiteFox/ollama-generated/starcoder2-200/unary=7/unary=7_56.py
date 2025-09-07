
class Model(torch.nn.Module):
    def __init__(self, l1=3):
        super().__init__()
        self.l = torch.nn.Linear(256*256, 8096)
 
    def forward(self, x1):
        v1  = self.l(x1) 
        v2 = (v1 * clamp(min=0, max=7, v1 + 3)).abs() / 7
        return torch.div(v2, 8)


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(4, 512*512)
