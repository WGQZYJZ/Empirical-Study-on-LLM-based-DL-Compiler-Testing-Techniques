
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 1)

    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        v3 = F.relu(v2)
        return v3

# Initializing the model
m = Model()
other = torch.tensor([0., 1.], dtype=torch.float, device='cuda')

# Inputs to the model
x  = torch.randn(5, 2048).to('cuda')
__output__  = m(x)

