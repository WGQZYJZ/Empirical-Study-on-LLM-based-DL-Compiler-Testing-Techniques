
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale=250., mask=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) /  sqrt(inv_scale) # Compute the dot product and scale it by a specified factor
        if not mask is None:
            scaled_dot_product += (mask * -torch.finfo(scaled_dot_product.dtype).max)
        attention_weights = scaled_dot_product.softmax(dim=-1)  # Apply softmax to the dot product, resulting in a set of weights 
        output = attention_weights.matmul(value) # Compute the final weighted sum by multiplying the value tensor with the set of attention weights
        return output

# Initializing the model
m  = Model()
