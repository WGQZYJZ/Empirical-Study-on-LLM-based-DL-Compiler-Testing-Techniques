
class Model(torch.nn.Module):
    def __init__(self, n_hidden=4, dim = 1):
        super().__init__()
        self.linear_0 = torch.nn.Linear(32*64, n_hidden)
        self.linear_1 = torch.nn.Linear(n_hidden, 8)
 
    def forward(self, x):
        v1 = x.view(-1, 32 * 64)
        v2 = self.linear_0(v1)
        v3 = self.linear_1(v2)
        v4 = torch.cat([v3], dim=dim)
        return v4


# Inputs to the model
x = torch.randn(8, 3, 64, 64)
