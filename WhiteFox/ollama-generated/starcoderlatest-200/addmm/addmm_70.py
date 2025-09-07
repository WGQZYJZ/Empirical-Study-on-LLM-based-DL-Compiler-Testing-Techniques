
class Model(torch.nn.Module):
    def __init__(self, inp = None):
        super().__init__()
        self.linear = torch.nn.Linear(512, inp)
 
    def forward(self, x1, inp = 0):
        v1 = torch.mm(x1, x2)
        v2 = v1 + inp
        return v2
# Initializing the model and the input tensor for it (this should be a random tensor!)
m = Model(inp=None)
x1 = torch.randn(1, 512, 32, 32)

