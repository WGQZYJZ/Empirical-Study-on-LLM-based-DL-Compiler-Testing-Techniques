
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, 2)
 
    def forward(self, x1):
        v0 = x1.view(-1, 3* 64 * 64).float()
        v1 = self.linear(v0)
        v2 = v1 - torch.tensor([[5., 5.]], dtype=torch.double).to(x1.device)
        v3 = F.relu(v2)
        return v3


# Initializing the model and its optimizer
m  = Model()
optimizer = torch.optim.SGD(m.parameters(), lr=0.5)


# Inputs to the model (the same as above)
x1 = torch.randn(4, 3 * 64 * 64).to(device)

__output__  = m(x1)

