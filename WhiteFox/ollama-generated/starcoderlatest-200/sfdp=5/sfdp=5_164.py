
class AttentionModel(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(num_heads=8, embed_dim=config['hidden_size'], dropout=0)
 
    def forward(self, x1, x2):
        _, attn_weight  = self.attn(x1, x2, x2) # Compute the attention weights
        return attn_weight

# Initializing the model
m = AttentionModel()
config = {
    'hidden_size': 64
}

# Inputs to the model
x1 = torch.randn(10, 3, config['hidden_size'], 256) # The input and query of shape (batch size, sequence length, dimension, head count), where the second last dimension represents the value tensor in each example.
x2 = torch.randn(10, 8, 256, config['hidden_size']) # The input and key of shape (batch size, num attention heads, query dimension, key dimension).
attn_weight = m(x1, x2)

