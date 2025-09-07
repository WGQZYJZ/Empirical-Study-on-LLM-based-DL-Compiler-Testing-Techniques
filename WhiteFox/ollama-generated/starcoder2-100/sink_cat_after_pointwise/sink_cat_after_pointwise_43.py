
class Model(torch.nn.Module):
    def __init__(self, dim=-1):
        super().__init__()

    def forward(self, t2):
        t3 = self.linear(t2)
        return t3


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(8)
x2  = torch.randn(5)
t1  = torch.cat([x1, x2], dim=0)
__output__  = m(torch.relu(t3))

 