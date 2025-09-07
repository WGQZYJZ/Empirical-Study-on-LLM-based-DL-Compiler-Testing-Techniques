
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn  = torch.nn.Linear(768, 32)
        self.out  = torch.nn.Linear(768, 10)
 
    def forward(self, query):
        k = torch.cat([self.attn(torch.zeros_like(query)), query], dim=-1)
        v  = torch.ones_like(k) * (-float('inf'))
 
        attn_mask = torch.full((32,), float('-inf'), dtype=torch.double)
        attn_mask[:0]  = 768 // 4
 
        a = torch.softmax(attn_weight, dim=-1)
        v1 = (k * a).sum(-1) + attn_mask
        v2  = self.out(v1)
        return v2

# Initializing the model
m  = Model()


# Inputs to the model<|end_of_input|>
x0, x1, x2 = torch.randn(64, 768), torch.randn(32, 768), torch.randn(32)
 
__output__   = m(x0)

