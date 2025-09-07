
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.multihead_attention = torch.nn.MultiheadAttention(
            embed_dim=768, num_heads=12, dropout=0.1
        )
 
    def forward(self, x1, x2, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1))
        qk = qk + attn_mask
        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ value
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(20, 64, 768)
x2 = torch.randn(20, 64, 768)
attn_mask = (torch.randn_like(x1) < 0.5).to(device)
