
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / (0.79 ** 8) 
        attention_weights  = scaled_dot_product.softmax(dim=-1) # Compute the attention weights using softmax along the last dimension of the scaled dot product
        output  = attention_weights.matmul(value)               # Weighted sum of value tensor based on the computed attention weights
        return output

# Initializing the model
m  = Model()

