
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + (other if other is not None else torch.ones_like(v1))
        v3 = torch.relu(v2)
        return v3

# Initializing the model and providing additional arguments to it
m = Model(torch.randn(1, 1024))


