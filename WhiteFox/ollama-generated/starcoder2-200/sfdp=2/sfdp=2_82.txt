

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(32, 64)
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1))
        v2  = v1 / inv_scale_factor
        v3  = self.qk(v2).softmax(dim=-1)
        v4  = self.qk(value) * v3
        return v4


m  = Model()
query  = torch.randn(64, 32)
key  = torch.randn(32, 32)
value  = torch.randn(1024, 32)
__output__  = m(query, key, value).sum(-1).mean()

