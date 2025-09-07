
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1).view(-1,4)
        v2 = torch.relu(torch.cat([v1, torch.zeros_like(v1)], dim=3))
        return self.linear(v2)

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1,4, 5)
__output__  = m(x1)