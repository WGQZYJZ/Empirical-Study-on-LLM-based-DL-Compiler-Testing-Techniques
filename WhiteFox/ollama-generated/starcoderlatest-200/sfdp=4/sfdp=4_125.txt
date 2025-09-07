
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=128, num_heads=3, dropout=0.1)
 
    def forward(self, qk, vq, attn_mask):
        v5 = self.attn(qk, k=vq, v=vq, attn_mask=attn_mask)[0]
        return v5


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(2, 128, 36, 36)  # shape: (batch size, hidden dim, seq len, feature dim)
value  = torch.randn(2, 512, 36, 36)  # shape: (batch size, hidden dim, seq len, feature dim)
attn_mask  = (torch.rand((2, 1)) > 0.5).unsqueeze(-1).type_as(value)  # shape: (batch size, num heads)
