
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(10, 5)
        self.m2 = torch.nn.Linear(4, 6)
 
    def forward(self, x1, x2):
        m1_out = self.m1(x1)
        m2_out = self.m2(x2)
        out  = (m1_out + m2_out) / 2
        return out


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 10)
x2 = torch.randn(4, 6)
