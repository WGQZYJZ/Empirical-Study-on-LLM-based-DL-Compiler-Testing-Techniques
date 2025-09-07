
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x1)
        if not hasattr(v1, '__isabstractmethod__'):
            t2 = v1 + inp
        return None
# Initializing the model
m = Model()

 # Inputs to the model
inp = torch.randn(8, 3, 64, 64)
x1 = torch.randn(512, 64, 64, dtype=torch.float32)
