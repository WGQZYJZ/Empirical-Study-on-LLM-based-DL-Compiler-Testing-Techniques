
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(3, 4)
        self.k = torch.nn.Linear(4, 4)
 
    def forward(self, x1):
        v1 = self.q(x1)
        v2 = self.k(v1)
        a  = (torch.matmul(x1, v2)) / math.sqrt(4*math.pi*4)
        b = torch.exp(-a)
        return b

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 3, 64, 64)
