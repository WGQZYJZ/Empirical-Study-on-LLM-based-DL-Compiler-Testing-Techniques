
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(768, 3072)
        self.attn_out = torch.nn.Linear(768, 768)
 
    def forward(self, x1):
        v1 = self.qk(x1)
        v2 = torch.matmul(v1, x1.transpose(-2, -1))
        v3 = v2 * 0.5
        v4 = v2 * 0.7071067811865476
        v5 = torch.erf(v4)
        v6 = v5 + 1
        v7 = v3 * v6
        return self.attn_out(v7)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3072, 1, 1)
