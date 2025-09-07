
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        attn_weights  = self.attention(q1, k1, v1)
        output         = attn_weights[0] @ attn_weights[2].transpose(-2, -1) / math.sqrt(attn_weights[1]) # Compute the dot product of attention weights and values, and scale it
        return output


# Inputs to the model
q1 = torch.randn(32, 64, 64)
k1 = torch.randn(32, 64, 64)
v1 = torch.randn(32, 64, 64)
