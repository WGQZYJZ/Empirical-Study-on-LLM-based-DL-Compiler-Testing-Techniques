
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(1, 8, 4)
 
    def forward(self, q, k, v):
        output, attention_weights = self.attention(q, k, v)
        return output
# Initializing the model
m = Model()

# Query tensor of shape (B, H, N, L), key tensor of shape (B, T, H, M), value tensor of shape (B, T, H, N)
query  = torch.randn(1024, 8, 64, 512)
key    = torch.randn(2048, 8, 256, 128)
value  = torch.randn(2048, 8, 256, 512)
