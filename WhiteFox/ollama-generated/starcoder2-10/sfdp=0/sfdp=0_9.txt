
class AttentionBlock(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale=None):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) 
        if not (scale is None or isinstance(scale, float)):
            raise TypeError("If `scale` is provided it should be of type float")
        if not (scale is None and len(query) == len(key)): 
            scaled_dot_product = scaled_dot_product / scale
 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value) 
        return output

# Initializing the model
m  = AttentionBlock()

 # Inputs to the model
 q1, k1, v1  = torch.randn(32, 512), torch.randn(32, 512), torch.randn(32, 8, 512)
 
 __output__  = m(q1, k1, v1)
