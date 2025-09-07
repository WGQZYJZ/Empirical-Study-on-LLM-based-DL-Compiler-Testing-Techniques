
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input = torch.nn.Linear(3, 8)

    def forward(self, x0):
        v1 = self.input(x0)
        return torch.cat([v1[:, :size], v1[:, size:]], dim=1).reshape(-1, 2 * 5)

# Initializing the model
m = Model()

 # Inputs to the model
x0 = torch.randn(49, 3, 8)
x1  = torch.randn(size, 7)
 
 # Outputs of the model
y  = m(torch.cat([x0[:, :size], x0[:, size:]], dim=1).reshape(-1, 2 * 5))

