
class Model2(torch.nn.Module):
    def __init__(self, m):
        super().__init__()
 
        self.linear = torch.nn.Linear(m ** 2, 100)
 
    def forward(self, x):
        v1 = self.linear(x)
        return torch.clamp(v1 + 3, min=0, max=6)/6

# Initializing the model with 500 hidden layer units
m = Model2(500)

