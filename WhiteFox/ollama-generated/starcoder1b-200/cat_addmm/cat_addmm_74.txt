
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.linear = torch.nn.Linear(n * 4, n)
 
    def forward(self, x1, x2):
        m = torch.addmm(x1, x1, x2)
        return self.linear(m)

# Initializing the model
m = Model(64)

