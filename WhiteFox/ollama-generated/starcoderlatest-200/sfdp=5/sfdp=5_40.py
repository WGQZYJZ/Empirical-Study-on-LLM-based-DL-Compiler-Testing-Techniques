
class MultiHeadAttention(torch.nn.Module):
    def __init__(self, d_model, nhead=128):
        super().__init__()
        self.d_model = d_model
        self.nhead = nhead
        self.attention = torch.nn.MultiheadAttention(d_model, nhead)
 
    def forward(self, query, key, value, attn_mask):
        return self.attention(query, key, value, attn_mask=attn_mask)[0]


# Initializing the model
m = MultiHeadAttention()

# Inputs to the model
x1 = torch.randn(32, 512, 64, 64)
