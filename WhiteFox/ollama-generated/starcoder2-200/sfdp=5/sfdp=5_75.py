
class Model(torch.nn.Module):
    def __init__(self, q_size, k_size=None):
        super().__init__()
        self.attn  = torch.nn.MultiheadAttention(q_size, k_size or q_size)
        self.norm1 = torch.nn.LayerNorm(q_size)
    
    def forward(self, x1):
        attn_mask = torch.triu(torch.ones((x1.shape[-2],  x1.shape[-2]), device=x1.device), diagonal=1)
        x2, _  = self.attn(
            query       = x1, 
            key         = x1, 
            value       = x1,
            attn_mask   = (1-attn_mask).unsqueeze(-3) 
        )
        return self.norm1(x2 + x1)


# Initializing the model
m  = Model(q_size=768)

# Inputs to the model