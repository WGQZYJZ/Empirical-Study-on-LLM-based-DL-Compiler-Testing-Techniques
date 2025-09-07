
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other_tensor 
        return v1


# Initializing the model
m2 = Model()
other_tensor = torch.randn(1, 8)

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
