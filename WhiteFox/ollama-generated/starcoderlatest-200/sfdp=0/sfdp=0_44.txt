
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=64, num_heads=1)
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(float(key.shape[-1])) # inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query, key, value = torch.randn(128, 64, 3, 64), torch.randn(128, 64, 3, 64), torch.randn(128, 64, 3, 64)
