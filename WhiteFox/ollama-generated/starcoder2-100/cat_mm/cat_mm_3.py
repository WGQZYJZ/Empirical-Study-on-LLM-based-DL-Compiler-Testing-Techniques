
class Model(torch.nn.Module):
    def __init__(self, d1):
        super().__init__()
        self.d  = d1
 
    def forward(self, x1):
        v1  = torch.mm(x1[0], x1[1])
        v2  = torch.cat([v1] * self.d)
        return v2


# Initializing the model
m  = Model(3)
 
# Inputs to the model
t1  = torch.randn(5, 4, 8)
t2  = torch.randn(5, 4, 8)
x1 = [t1, t2]
