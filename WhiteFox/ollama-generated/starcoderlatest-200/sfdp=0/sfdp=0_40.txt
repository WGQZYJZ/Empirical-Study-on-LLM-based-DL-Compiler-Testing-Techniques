
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1, scale_factor=None):
        scaled_dot_product = torch.matmul(q1, k1.transpose(-2, -1)) / (scale_factor ** 0.5) # Apply softmax to the dot product of query and key, and then divide by square root of dimensions of query and key vectors
        attention_weights = scaled_dot_product.softmax(dim=-1) # Compute a softmax probability distribution on the dot products of each query vector with all other query vectors
        output = attention_weights.matmul(v1) # Apply the weights to value tensor, and then concatenate them in the same shape as input tensors
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = ScaledDotProductAttention()
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = self.attention(q1=v2, k1=v2, v1=x1, scale_factor=1.0 / (self.conv.out_channels ** 0.5))
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
