
class Model(torch.nn.Module):
    def __init__(self, inp=10):
        super().__init__()
        self.inp = torch.tensor([inp], dtype=torch.float)
 
    def forward(self, x1, x2):
        return x1 * 2 + self.inp
 
 
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
