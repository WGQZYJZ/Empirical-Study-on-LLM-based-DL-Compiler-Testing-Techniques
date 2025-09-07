
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.t1 = torch.nn.Parameter(torch.randn(3, 4))
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return v1 + self.t1

# Initializing the model
m = Model()


