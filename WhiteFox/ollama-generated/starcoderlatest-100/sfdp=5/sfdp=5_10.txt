
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 16, bias=False)
 
    def forward(self, x1):
        v1 = self.qkv(x1)
        qk = v1[:, :8, :]
        key = v1[:, 8:, :]
        v2 = torch.einsum("bnhcd,bchd->nbhc", (qk, key)).transpose(-2, -1).contiguous()
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
