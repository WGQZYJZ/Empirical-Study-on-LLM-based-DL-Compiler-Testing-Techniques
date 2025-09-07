
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=10, num_heads=2)
 
    def forward(self, q, k, v):
        o  = self.attn(q, k, v)[0]
        return o


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(64, 256) # Query tensor of shape [batch_size, head_size * num_heads]
x3  = torch.randn(64, 2560) # Value tensor of shape [batch_size, value_sequence_length, head_size * num_heads]
x2  = torch.randn(64, 10, 64) # Key tensor of shape [batch_size, head_size * num_heads, key_sequence_length]
 

