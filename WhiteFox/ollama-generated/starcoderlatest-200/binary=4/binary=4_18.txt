
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m2 = Model2()

# Inputs to the model (Note: the input tensor should be different from the previous one!)
x1 = torch.randn(1, 3, 64, 64)
