class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 * 0.5 
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3) + 1
        v5  = v2 * v4
        return v5


m  = Model()
