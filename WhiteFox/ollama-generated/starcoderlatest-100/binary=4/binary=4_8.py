
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.shape[0], -1))
        v2 = v1 + other
        return v2


# Inputs to the model
x1 = torch.randn(1, 3 * 64 * 64)
other = torch.rand(1, 50)
