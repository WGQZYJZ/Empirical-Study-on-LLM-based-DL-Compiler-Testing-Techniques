
class SelfAttention(torch.nn.Module):
    def __init__(self, embed_dim, head_dim, num_heads, dropout=0.1):
        super().__init__()
        self.self_attn = torch.nn.MultiheadAttention(embed_dim, head_dim, num_heads)
        self.norm1 = torch.nn.LayerNorm(embed_dim, eps=1e-6, elementwise_affine=True)
        self.dropout = torch.nn.Dropout(p=dropout)

    def forward(self, x):
        # Scaled Dot-Product Attention (https://arxiv.org/abs/1706.03762)
        q, k, v = x[0], x[1], x[2]  # query, key, value
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.size(-1))

        attention_weights = self.self_attn(scaled_dot_product)[0]

        x = attention_weights @ v
        x = self.dropout(x)
        x = self.norm1(x + q)
        
        return x

# Initializing the model
m = SelfAttention()

 # Inputs to the model
x = torch.randn(2, 3, 64, 64)
