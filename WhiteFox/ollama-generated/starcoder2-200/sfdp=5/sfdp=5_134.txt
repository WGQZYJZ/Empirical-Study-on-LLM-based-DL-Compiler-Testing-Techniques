
class Model(torch.nn.Module):
    def __init__(self, num_heads=4):
        super().__init__()
        self.num_heads  = num_heads
 
    def forward(self, query, key, value):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk  = qk + attn_mask # where attn_mask is the attention mask
        attn_weight  = torch.softmax(qk, dim=-1)
        attn_weight  = torch.dropout(attn_weight, dropout_p, True) 
        output   = attn_weight @ value
class Model(torch.nn.Module):
    def __init__(self, num_heads=4):
        super().__init__()
        self.num_heads  = num_heads
 
    def forward(self, query, key, value):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk  = qk + attn_mask # where attn_mask is the attention mask
        attn_weight  = torch.softmax(qk, dim=-1)
        attn_weight  = torch.dropout(attn_weight, dropout_p, True) 
        output   = attn_weight @ value


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(8, 320, 64)
key    = torch.randn(1572864, 128)
value  = torch.randn(1572864, 64)

