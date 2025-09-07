
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output             = attention_weights.matmul(value)
        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention_layer = ScaledDotProductAttention()
 
    def forward(self, query, key, value, inv_scale=None):
        attention_output = self.attention_layer(query, key, value, inv_scale)
        return attention_output

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
y1  = torch.randn(1, 8, 64, 64)
z1  = torch.randn(1, 8, 64, 64)
inv_scale = torch.randn([1]) # Scaling factor `inv_scale` is typically the square root of the dimension of the key/query vectors
