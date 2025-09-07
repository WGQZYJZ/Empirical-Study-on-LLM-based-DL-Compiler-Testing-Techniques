
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other
        return v6


# Initializing the model with input tensor and keyword argument other
m2 = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
other = torch.tensor([0.5])
