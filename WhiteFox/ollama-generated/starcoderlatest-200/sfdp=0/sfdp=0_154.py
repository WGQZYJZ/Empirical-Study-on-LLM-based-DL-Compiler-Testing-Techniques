
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, attention_dim=None):
        super().__init__()
        self.attention_dim = attention_dim
 
    def forward(self, query, key, value, scaled_dot_product_matrix=None, inv_scale=None):
        if scaled_dot_product_matrix is None:
            if self.attention_dim is not None:
                query = query.reshape(-1, self.attention_dim)
                key = key.reshape(-1, self.attention_dim)
                value = value.reshape(-1, self.attention_dim)
                scaled_dot_product_matrix = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
            else:
                scaled_dot_product_matrix = torch.matmul(query, key.transpose(-2, -1))
        attention_weights  = scaled_dot_product_matrix.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output
 
 class Model(torch.nn.Module):
    def __init__(self, attention_dim=None):
        super().__init__()
        self.attention_dim = attention_dim
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.attention = ScaledDotProductAttention(attention_dim)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = self.attention(v1)
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
