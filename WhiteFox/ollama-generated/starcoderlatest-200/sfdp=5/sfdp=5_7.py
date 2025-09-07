
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, attn_mask):
        k = k.transpose(-2, -1) / math.sqrt(k.size(-1))
        qk = q @ k
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ v
        return output


# Inputs to the model
query = torch.randn(5, 8, 64, 64)
key = torch.randn(32, 16, 32, 32)
value = torch.randn(32, 16, 32, 32)
attn_mask = torch.ones(5, 32).bool() # Attention mask should be broadcastable to the shape of query (i.e. 5 x 8)
