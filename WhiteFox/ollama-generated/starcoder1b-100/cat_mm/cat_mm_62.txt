
class Model(torch.nn.Module):
    def __init__(self, dim_a: int, dim_b: int = 2):
        super().__init__()
        self.dim_a = dim_a
        self.dim_b = dim_b
        self.mat = torch.randn([3 * self.dim_a * self.dim_b])

    def forward(self, x1, x2):
        v1  = x1
        v2 = torch.cat([x1, x1, x1], -1)
        v3 = torch.cat([v1, v2, v2], -1)
        return torch.mm(v3, self.mat)


# Initializing the model
m = Model(4)


# Inputs to the model
x1 = torch.randn(3, 5, 30, 30)
x2 = torch.randn(10, 3, 18, 18)
