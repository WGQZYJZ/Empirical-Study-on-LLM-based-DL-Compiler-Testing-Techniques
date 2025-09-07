
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.fc = torch.nn.Linear(784, 10)

    def forward(self, x1): 
        v1 = torch.addmm(x1, self.weight.t(), self.bias)
        v2 = torch.cat([v1], dim)
        return v2

# Initializing the model
m = Model(dim=0)

