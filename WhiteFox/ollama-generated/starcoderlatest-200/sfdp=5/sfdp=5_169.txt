
class Model(torch.nn.Module):
    def __init__(self, dim_in=768, dim_out=1000, nhead=4):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            num_heads=nhead,
            embed_dim=dim_in,
            dropout=0.05)  # Use attention with 4 heads, and use the number of tokens in each token type to compute attention weights

    def forward(self, query, key, value, attn_mask):
        qk = self.attn(query, key, value,
                        attn_mask)[0]  # Attention: [bs * sl1, dim_in], [bs * sl2, dim_in] -> [bs * sl1, bs * sl2]
        output = torch.matmul(qk, value)  # [bs * sl1, bs * sl2], [dim_in, dim_out]
        return output

# Initializing the model
m = Model(dim_in=768, dim_out=1000, nhead=4)
query = torch.randn(1, 32, 1536) # [1, sl1, dim]
key = torch.randn(1, 32, 512)   # [1, sl2, dim]
value = torch.randn(1, 32, 768)  # [1, sl2, dim]
attn_mask = torch.ones([1, 1536]) # Mask for attention with only 1 token in each sequence (sl1=1, sl2=2)
