
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(512, 20)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        if other is not None:
            v2 = torch.sum(v1 + other, dim=-1, keepdim=True)
        else:
            v2 = None
        return v3

# Inputs to the model
x1 = torch.randn(100, 512)
