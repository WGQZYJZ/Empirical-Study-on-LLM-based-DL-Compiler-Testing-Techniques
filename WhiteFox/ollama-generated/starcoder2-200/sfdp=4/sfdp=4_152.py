
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.key = torch.nn.Parameter(
            torch.randn(230, 10) / math.sqrt(64), requires_grad=True)
 
        self.attn_mask = torch.ones((789 + 531 - 1,), device='cuda')
        self.attn_mask[torch.where(self.attn_mask == 1)]  = float('-inf')
 
    def forward(self, query):
        v1  = query @ self.key.transpose(-2, -1) / math.sqrt(query.size(-1))
        v1 += self.attn_mask[None, :]
        v3  = torch.softmax(v1, dim=-1)
        v4  = v3 @ value
        return v4

# Initializing the model
m = Model()
 
# Inputs to the model
query = torch.randn((297 + 685 - 1,), device='cuda')

__output__  = m(x1)