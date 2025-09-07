
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        if other is not None and other.shape != (4,):
            raise ValueError("Invalid shape of argument 'other'.")
        self.linear = torch.nn.Linear(32, 64)
        self._register_parameter('other', other)
 
    def forward(self, x1: torch.Tensor, other: torch.Tensor):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64, 64)
other = torch.rand(4,)
