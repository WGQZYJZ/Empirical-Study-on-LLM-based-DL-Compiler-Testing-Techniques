
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
attention_module  = ScaledDotProductAttention()

 # Inputs to the model
query  = torch.randn(1, 3, 64, 64)
key    = torch.randn(1, 3, 64, 64)
value  = torch.randn(1, 8, 64, 64)

 # Output of the model
scaled_dot_product  = attention_module(query, key, value, scale)
output             = scaled_dot_product
 
