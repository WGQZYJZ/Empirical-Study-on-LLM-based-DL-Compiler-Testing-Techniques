
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) * 0.5
        v2 = (self.linear(x1) * (self.linear(x1)) * (self.linear(x1))) * 0.044715
        v3 = ((torch.ones_like(v1)) * 0.7978845608028654).cuda()
        v4 = torch.tanh(v2) + (torch.ones_like(v1))) * 1e-6
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(1, 32)
