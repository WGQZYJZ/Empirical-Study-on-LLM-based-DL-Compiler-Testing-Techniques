
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(embed_dim=8, num_heads=4)
 
    def forward(self, x1, x2, mask):
        query  = x1
        key    = x2
        output, attention = self.attention(query, key, x2, attn_mask=mask)
        return output


# Inputs to the model
x1 = torch.randn(8, 3, 64, 64) # Query
x2 = torch.randn(5, 3, 64, 64) # Key
mask = torch.tensor([[True, True, False, False], 
                     [False, True, True, True], 
                     [False, False, True, True]]) # Attention mask
