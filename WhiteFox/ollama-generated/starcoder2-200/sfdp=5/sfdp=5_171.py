

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(0.1 * torch.randn(32, 64))
 
    def forward(self, key, value):
         qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
         qk = qk + attn_mask # 96 96
         attn_weight = torch.softmax(qk, dim=-1)
         attn_weight = torch.dropout(attn_weight, dropout_p, True)
         output = attn_weight @ value
        return output

# Initializing the model
m = Model()
 
# Inputs to the model
key  = torch.randn(32, 64, 800) # size of 32 * 64 * 800
value = key
attn_mask  = torch.ones(100, 96, 96).to(key.device)
 
# Initializing the model with parameters
m = Model()
m(key, value, attn_mask)

