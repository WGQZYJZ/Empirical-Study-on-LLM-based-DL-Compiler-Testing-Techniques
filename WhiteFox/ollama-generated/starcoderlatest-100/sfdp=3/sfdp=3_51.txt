
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(
            embed_dim=64, num_heads=8)

    def forward(self, q1, k1, v1):
        v2, attn  = self.attn(q1, k1, v1) # Use Multihead attention to compute the values of all heads
        softmax_v2 = torch.nn.functional.softmax(attn, dim=-1) # Apply softmax to the output from Multihead attention
        output = softmax_v2.matmul(v1) # Compute the dot product between the softmax and value vectors
        return output

# Inputs to the model
q1 = torch.randn(4, 64, 3, 1024) # Query
k1 = torch.randn(4, 64, 8, 512) # Key
v1 = torch.randn(4, 64, 8, 512) # Value
