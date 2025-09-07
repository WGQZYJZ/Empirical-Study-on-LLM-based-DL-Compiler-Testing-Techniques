
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=64):
        super().__init__()
 
    def forward(self, query, key, value, mask=None, inv_scale=None):
        # Replace with implementation from previous exercise:
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        if mask is not None:
            # Apply the mask to the softmax output.
            attention_weights = attention_weights * mask
        return attention_weights.matmul(value)
 

class Model(torch.nn.Module):
    def __init__(self, dim=64):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = ScaledDotProductAttention(dim)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        v7 = self.attention(query=v6, key=v6, value=v6, inv_scale=0.95)
        return v7

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=64):
        super().__init__()
 
    def forward(self, query, key, value, mask=None, inv_scale=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        if mask is not None:
            attention_weights = attention_weights * mask
        return attention_weights.matmul(value)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
