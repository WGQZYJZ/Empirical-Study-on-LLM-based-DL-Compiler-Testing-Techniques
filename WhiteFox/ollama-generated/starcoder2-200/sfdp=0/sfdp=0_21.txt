
class Model(torch.nn.Module):
    def __init__(self,  inv_scale=1):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)  # Apply Softmax to the attention weights
        output = attention_weights.matmul(value)
        return output

# Initializing the model