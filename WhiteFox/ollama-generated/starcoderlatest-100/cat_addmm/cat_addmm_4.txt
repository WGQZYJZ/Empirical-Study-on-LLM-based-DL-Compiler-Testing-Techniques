
class Model(torch.nn.Module):
    def __init__(self, dim=-1):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 512)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model(dim=1)
 
# Inputs to the model
x = torch.randn(64, 1, 28, 28)
