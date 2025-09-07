
class Attention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = Attention(8)
 
    def forward(self, x1, key, value):
        v6  = self.attention(x1, key, value) # Apply attention to the input tensor
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key  = torch.randn(8, 256, 64, 64)
value = torch.randn(8, 256, 64, 64)
