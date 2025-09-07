
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l = torch.nn.Linear(32*32, 10)
 
    def forward(self, x1):
        v1 = self.l(x1.view(-1))
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
