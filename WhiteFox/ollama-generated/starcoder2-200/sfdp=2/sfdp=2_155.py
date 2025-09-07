
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=32, num_heads=8)
 
    def forward(self, x1):
        v1  = self.attention(x1, x1)[0] 
        return v1

# Initializing the model