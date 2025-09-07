
class AttentionModel(torch.nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        self.attn = torch.nn.Linear(embed_dim, embed_dim)
 
    def forward(self, q, k, v, mask=None):
        # Compute the dot product of q and k, and scale it
        k = k / math.sqrt(k.size(-1)) 
        attn_weight = self.attn(torch.cat([q, k], dim=-1))
        if mask is not None:
            attn_weight += (mask + torch.eye(attn_weight.shape[-2]).to(attn_weight.device)) / 2
        
        # Apply softmax to the result
        attn_weight = torch.softmax(attn_weight, dim=-1)
        attn_weight = torch.dropout(attn_weight, dropout_p, True)
        output = attn_weight @ v 
        return output


# Initializing the model
m = AttentionModel(embed_dim=8)

# Inputs to the model
q = torch.randn(1, 32, 64, 64)
k = torch.randn(8, 32, 64, 64)
v = torch.randn(8, 32, 64, 64)
mask = torch.eye(attn_weight.shape[-2]).to(attn_weight.device)
