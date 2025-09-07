
class Model(torch.nn.Module):
    def __init__(self, attn_mask=None):
        super().__init__()
        self.attn_mask = attn_mask
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk += self.attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value
        return output


# Inputs to the model
query  = torch.randn(2048, 512, 64, 64)
key    = torch.randn(2048, 512, 64, 64)
value  = torch.randn(2048, 512, 64, 64)
