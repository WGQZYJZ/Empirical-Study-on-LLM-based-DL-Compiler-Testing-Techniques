
class Attention(torch.nn.Module):
    def __init__(self, dim, inv_scale=None):
        super().__init__()
 
        self._scale = 1 / math.sqrt(dim) if inv_scale is None else inv_scale
 
    def forward(self, query, key, value):
         # Scaled dot-product attention
         scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) * self._scale 
         attention_weights  = scaled_dot_product.softmax(dim=-1)
         output  = attention_weights.matmul(value)
         return output
 
# Initializing the model
m = Attention(768, 768 ** 0.5)

 # Inputs to the model
query  = torch.randn(32, 64, 768)
key   = torch.randn(32, 192, 768)
value = torch.randn(32, 192, 768)

 