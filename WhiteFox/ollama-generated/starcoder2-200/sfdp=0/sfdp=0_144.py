
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=0.25):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale # The scaled dot product calculation: scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) * 4 # Adding a scaling factor to the attention weights
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value) 
        return output


# Initializing the model
attn  = Attention()


# Inputs to the model
q  = torch.randn(2, 64, 500, 897) # The size of query is (batch, heads, length_query, length_key)
k  = torch.randn(31, 64, 500, 897) # The size of key is (batch, heads, length_key, length_query)
v  = torch.randn(23, 64, 897, 800) # The size of value is (batch, heads, length_value, length_query)


