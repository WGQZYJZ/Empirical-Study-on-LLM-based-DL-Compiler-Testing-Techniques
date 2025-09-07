
class Model(torch.nn.Module):
    def __init__(self, dim_k=512, dim_v=256, d_ff=1024, nhead=8):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm(dim_k)
        self.attn = torch.nn.MultiheadAttention(embed_dim=dim_k, num_heads=nhead, dropout=0.1)
 
    def forward(self, x):
        y = self.layer_norm(x)
        q, k, v = torch.chunk(y, 3, dim=-1)
        attn_weights = self.attn(q, k, value=v)[0]
        output = torch.cat([attn_weights, y], -1) # Concatenate the attention weights and outputs
        return output


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(32, 512, 16, 16)
