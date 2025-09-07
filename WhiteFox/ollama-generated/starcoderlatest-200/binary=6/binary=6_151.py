
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other_tensor
        return v2


# Initializing the model
m2 = Model2()
# Inputs to the model
other_tensor = torch.tensor([0.0])
x1 = torch.randn(1, 3, 64, 64)
