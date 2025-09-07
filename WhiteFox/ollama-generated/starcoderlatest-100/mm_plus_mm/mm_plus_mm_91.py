
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(2, 3)
 
    def forward(self, x):
        v1 = torch.mm(x[0], x[1])
        v2 = torch.mm(x[2], x[3])
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x  = [torch.randn(5, 7),
      torch.randn(5, 9), 
      torch.randn(64 * 10, 28 * 28)]
