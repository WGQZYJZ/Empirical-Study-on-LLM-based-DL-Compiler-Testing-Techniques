
class Model(torch.nn.Module):
    def __init__(self, n_heads, d_model, dropout=0.1):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=d_model, num_heads=n_heads
        )  # Construct an MHA object with input dimension and number of attention heads
 
    def forward(self, query, key, value, attn_mask):
        qk = self.attn(query, key, value)[0]
        output = torch.matmul(attn_weight, value)
        return output


# Initializing the model
m = Model(n_heads=2, d_model=768)
x1 = torch.randn(1, 1536, 768)
x2 = torch.randn(1, 1536, 768)
x3 = torch.randn(1, 1536, 768)
attn_mask = torch.zeros((1, 1536, 768)) # Construct a zero attention mask of size (batch size, sequence length, embedding dimension).
