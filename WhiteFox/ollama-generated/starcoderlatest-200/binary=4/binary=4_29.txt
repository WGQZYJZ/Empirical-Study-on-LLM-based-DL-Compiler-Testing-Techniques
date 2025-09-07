
class Model(torch.nn.Module):
    def __init__(self, other_tensor):
        super().__init__()
        self.linear = torch.nn.Linear(80, 32)
        self.other_tensor = other_tensor
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other_tensor
        return v6


# Initializing the model and passing it an input tensor as an argument
m = Model(torch.ones(80))
x1 = torch.randn(1, 3, 64, 64)
