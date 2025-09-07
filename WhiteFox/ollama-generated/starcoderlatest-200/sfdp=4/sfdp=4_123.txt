
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=8, num_heads=4)

    def forward(self, x1, x2, mask=None):
        q  = x1 
        k  = x2
        v  = x2
        out, attn = self.attn(q, k, v, need_weights=True) # Apply multi-head attention to the query and key tensors

        if mask is not None:
            out = out * mask
            
        return out


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(4, 3, 64, 64)
x2  = torch.randn(8, 3, 64, 64)
mask=torch.ones((1, 1, x1.shape[2], x1.shape[3]))  # Input mask to prevent attention to certain positions (e.g., padding).
