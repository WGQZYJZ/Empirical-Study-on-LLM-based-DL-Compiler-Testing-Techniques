
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 64) 
        self.key   = torch.nn.Linear(3, 64)
 
    def forward(self, query, key, attn_mask):
        qk = self.matmul(query, key)
        qk = qk / math.sqrt(qk.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = torch.matmul(attn_weight, value)
        return output


# Inputs to the model
query  = torch.randn(1, 3, 64, 64)
key    = torch.randn(1, 3, 64, 64)
attn_mask = (attn_mask == -1e9).type(torch.float)
