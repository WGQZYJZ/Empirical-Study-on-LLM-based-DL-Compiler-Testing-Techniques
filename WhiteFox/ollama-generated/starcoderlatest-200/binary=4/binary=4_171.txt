
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(x1.shape[0], -1))
        v2 = v1 + other
        return v6


# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 3 * 64 * 64)
