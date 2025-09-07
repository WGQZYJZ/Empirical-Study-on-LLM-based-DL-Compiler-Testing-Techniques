
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x):
        v  = self.linear(x) + torch.rand_like(v) * 0.5
        return v

# Initializing the model
m = Model()

 # Inputs to the model
__input__ = torch.randn(1, 128)
other = torch.randn(3, 64)
