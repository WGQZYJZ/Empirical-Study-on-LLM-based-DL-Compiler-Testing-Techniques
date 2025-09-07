
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=1.0):
        super().__init__()
        self.inv_scale = 2 ** (- (0.5 / inv_scale))
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) * self.inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
m  = ScaledDotProductAttention()
 
  # Inputs to the model
query  = torch.randn(2, 3, 640)
key   = torch.randn(1, 128, 5)
value = torch.randn(7, 9, 640)
 
__output__  = m(query, key, value)

