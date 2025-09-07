
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1): 
        scale  =  50e-4 # A hyperparameter to tune the attention
        v1  = torch.randn(32)
        k1  = torch.randn(32)
        q1  = torch.randn(32)
        output  =  self._scaled_dot_product_attention(q1, k1, v1)
        return output
 
    @staticmethod
    def _scaled_dot_product_attention(query, key, value):
        # Compute the dot product of the query and key tensors
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1))
        scaled_dot_product  /= math.sqrt(key.shape[-1])
        # Apply softmax to the scaled dot product
        attention_weights  = scaled_dot_product.softmax(dim=-1)
 
        # Compute the output by multiplying the value and attention weights
        output  = torch.matmul(attention_weights, value)
        return output


# Initializing the model