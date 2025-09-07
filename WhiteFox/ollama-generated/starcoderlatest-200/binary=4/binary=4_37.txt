
class Model(torch.nn.Module):
    def __init__(self, other_tensor: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.other = other_tensor
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        return v2


# Initializing the model with an additional tensor
m = Model(torch.randn(1, 3, 64, 64))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
