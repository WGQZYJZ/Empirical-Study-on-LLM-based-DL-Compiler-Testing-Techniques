
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2560, 43)

    def forward(self, x1):
        v1 = self.linear(x1) + other
        v2 = F.relu(v1)
        return v2

# Initializing the model
m = Model()

# Inputs to the model
other = torch.randn(3, 43).to('cuda:0')
x1   = torch.randn(784, 5, device='cuda', dtype=torch.double)

__output__  = m(x1)

