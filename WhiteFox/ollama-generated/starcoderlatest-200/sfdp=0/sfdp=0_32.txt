
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m  = Attention()

 # Inputs to the model
  query = torch.randn(batch, num_heads, seq_len, dim)
  key = torch.randn(batch, num_heads, seq_len, dim)
  value = torch.randn(batch, num_heads, seq_len, dim)
  