
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model(other_tensor=torch.randn(2, 3))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
