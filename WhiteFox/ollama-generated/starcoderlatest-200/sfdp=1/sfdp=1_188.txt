
class Attention(torch.nn.Module):
    def __init__(self, query_channel, key_channel, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
        self.attention  = torch.nn.MultiheadAttention(query_channel, key_channel, num_heads=num_heads)
    
    def forward(self, query, key):
        qk = self.attention(query, key)
        return qk

# Initializing the model
m = Attention(16, 32, 8)

 # Inputs to the model
x1 = torch.randn(1, 8, 16)
