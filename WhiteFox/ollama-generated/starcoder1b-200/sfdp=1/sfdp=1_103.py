
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(5, 8)
        self.key = torch.nn.Linear(7, 10)
        self.value = torch.nn.Linear(3, 20)
        self.scale_factor = torch.nn.Parameter(torch.ones(8))

    def forward(self, x):
        q  = self.query(x).reshape(-1, 5, 8)
        k  = self.key(x).reshape(-1, 7, 10)
        v  = self.value(x).reshape(-1, 3, 20)
        dk = torch.einsum("ncd,ncd->nc", k, x).softmax(dim=-1).div(self.scale_factor).unsqueeze(dim=2)
        return dk.matmul(v)


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(10, 3, 64, 64)
__output__  = m(x)


