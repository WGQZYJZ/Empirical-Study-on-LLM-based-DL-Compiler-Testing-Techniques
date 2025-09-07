
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Apply dropout to the result of applying softmax
        query = torch.randn(5) @ torch.randn(7).t() + torch.randn(7) * 0.2
        key = torch.randn(5) @ torch.randn(3).t() + torch.randn(3) * 0.4
        value = torch.randn(10, 3)
 
        attn_mask = torch.ones(query.size(-2), query.size(-1)) - torch.eye(query.size(-2), query.size(-1)) 
        dropout_p = float(torch.randint(0, 5, ()).item() + 1) / 3
        qk = query @ key.t()
        qk = qk / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-2)
        attn_weight = torch.dropout(attn_weight, dropout_p, True) 
        output  = attn_weight @ value
        return output
 
# Initializing the model