
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 8)
        self.key   = torch.nn.Linear(64, 8)
 
    def forward(self, query_vec, key_vec, attn_mask):
        qk = query_vec @ key_vec.transpose(-1, -2) / math.sqrt(query_vec.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()


# Inputs to the model
query_vec  = torch.randn(64, 32)
key_vec    = torch.randn(64, 16)
attn_mask  = torch.randn(64, 64)
