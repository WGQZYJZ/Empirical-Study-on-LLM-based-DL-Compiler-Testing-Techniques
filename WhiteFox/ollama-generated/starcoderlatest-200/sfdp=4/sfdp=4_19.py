
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=16, num_heads=8)
 
    def forward(self, qk, attn_mask):
        v1, _, _ = self.attention(qk, qk, key_padding_mask=attn_mask, output_attentions=True)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(16, 16, 32, 32)
attn_mask = torch.ones((16, 16, 32, 32))
