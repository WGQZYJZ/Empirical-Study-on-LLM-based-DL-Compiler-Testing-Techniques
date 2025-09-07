
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        v1 = self.linear(x) - torch.tensor(0.5, dtype=torch.double, device='cuda')
        return v1

# Initializing the model
m = Model()

