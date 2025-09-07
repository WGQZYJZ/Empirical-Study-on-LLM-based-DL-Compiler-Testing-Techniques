
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=None):
        super().__init__()
        self.inv_scale = inv_scale

    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
         scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale
         attention_weights = scaled_dot_product.softmax(dim=-1)
         output  = attention_weights.matmul(value)
         return output

# Initializing the model
m  = ScaledDotProductAttention()

 # Inputs to the model
query = torch.randn((5,4))
key   = torch.randn((3,2,5,7))
value = torch.randn((8,10,9))
 
output_from_the_model = m(query, key, value)
