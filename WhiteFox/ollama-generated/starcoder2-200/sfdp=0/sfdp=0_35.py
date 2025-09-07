
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=None):
        super().__init__()
        self.inv_scale = inv_scale
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale if self.inv_scale else torch.matmul(query, key.transpose(-2, -1))
        attention_weights  = scaled_dot_product.softmax(dim=-1) 
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
m  = ScaledDotProductAttention() # Use None as a default value for inv_scale (to disable scaling in the dot product)


# Inputs to the model
query  = torch.randn(32, 64, 8)
key  = torch.randn(32, 10, 8)
value  = torch.randn(32, 5, 16)
__output__  = m(query, key, value)

