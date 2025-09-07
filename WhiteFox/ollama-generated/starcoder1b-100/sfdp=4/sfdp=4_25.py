
class Model(torch.nn.Module):
    def __init__(self, n_heads, d_k, d_v, max_length=512, dropout=0.25):
        super().__init__()
        self.query = torch.nn.Linear(d_v, n_heads * d_k)
        self.key   = torch.nn.Linear(d_v, n_heads * d_k)
        self.value  = torch.nn.Linear(d_v, n_heads * d_k)
        self.proj   = torch.nn.Linear(n_heads * d_k, d_v)
        self.dropout = nn.Dropout(p=dropout)
 
    def forward(self, x1, x2):
        q   = self.query(x1)
        k   = self.key(x2)
        v   = self.value(x2)
        attn_weight  = torch.softmax(q @ k.transpose(-2, -1) / math.sqrt(k.size(-1)), dim=-1)
        output        = attn_weight @ v
        return self.dropout(output)


# Initializing the model
m = Model(8, 32, 64, dropout=0.25)

