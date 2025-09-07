
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.attention_layer = torch.nn.MultiheadAttention(embed_dim=hidden_size)
 
    def forward(self, q, k, v, mask=None):
        output, _  = self.attention_layer(q, k, v, need_weights=False, attn_mask=mask) 
        return output


# Initializing the model
m = Model(hidden_size)

# Inputs to the model
q = torch.randn(1, 3, hidden_size, 64)
k = torch.randn(1, 3, hidden_size, 64)
v = torch.randn(1, 3, hidden_size, 64)
mask = None
