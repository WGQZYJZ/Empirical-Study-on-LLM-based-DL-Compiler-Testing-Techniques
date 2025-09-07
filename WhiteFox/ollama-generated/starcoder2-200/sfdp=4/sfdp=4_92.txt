
class Attn(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, attn_mask=None):
        qk  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1))
 
        if isinstance(attn_mask, (torch.Tensor)):
            attn_mask = attn_mask * (-1e9)
            qk += attn_mask
        attn_weight  = torch.softmax(qk, dim=-1)
        output = torch.matmul(attn_weight, value)
        return output
 
# Initializing the model
m  = Attn()


# Inputs to the model
query  = torch.randn(32, 64)
key = torch.randn(32, 1024)
value = torch.randn(32, 1024)

