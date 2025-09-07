
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.5, attn_mask=""):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=32, num_heads=8)
 
    def forward(self, query, key, value, mask):
        out1  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        out2  = out1 + torch.nn.functional.softmax(mask * 30., dim=-1).dropout() 
        return attn_weight @ value


# Initializing the model
m = Model(dropout_p=0.5, attn_mask="")

