
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 2)
 
    def forward(self, x1, x2):
        v1 = self.attention(x1, x2, x2)[0] # Output of the Multihead Attention
        v2 = (v1 * 0.5 + v1 * 0.7071067811865476) / torch.sqrt(x1.shape[1])  # Attention weights from Softmax are divided by sqrt(dim_of_keys)
        v3 = (v2 * x1 + v2 * v1) # Apply pointwise multiplication on attention weights with query tensor, which is input to the Multihead Attention
        return v3


# Initializing the model
m = AttentionModel()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64) # Query tensor
x2 = torch.randn(1, 8, 64, 64) # Key tensor
