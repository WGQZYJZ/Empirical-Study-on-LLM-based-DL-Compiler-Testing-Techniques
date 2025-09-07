
class SelfAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 1./ math.sqrt(2048) # In the BART Transformer model, 2048 is the embedding dimension, and it's used as the scaling factor.
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.scale
        attention_weights = scaled_dot_product.softmax(dim=-1) # Softmax normalization is applied to the last dimension (-1). This normalizes each row of the tensor so that they sum up to 1.
        output  = attention_weights.matmul(value)
        return output


# Initializing the model