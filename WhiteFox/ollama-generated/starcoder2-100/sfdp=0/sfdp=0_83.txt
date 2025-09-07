

class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value):  # Forward function for Scaled Dot-Product Attention.
        scaled_dot_product = torch.matmul(
            query, 
            key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1) 
        output = attention_weights.matmul(value)  # Computing the attention output as a weighted sum of value tensor.
        return output


# Initializing and testing the model.
m  = Attention() 
 