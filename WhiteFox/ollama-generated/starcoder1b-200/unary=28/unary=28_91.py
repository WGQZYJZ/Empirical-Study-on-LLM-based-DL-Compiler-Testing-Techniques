
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=10):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m  = Model()
m.eval() # Turn off gradients during forward pass to allow checking correctness
__input__ = torch.randn(1, 32)
x1 = __input__.cuda() if torch.cuda.is_available() else __input__
