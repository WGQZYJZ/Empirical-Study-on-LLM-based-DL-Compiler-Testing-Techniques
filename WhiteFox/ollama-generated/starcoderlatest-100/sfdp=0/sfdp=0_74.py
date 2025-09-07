
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, query, value, key, inv_scale):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / inv_scale
        attention_weights    = scaled_dot_product.softmax(dim=-1)
        output               = attention_weights.matmul(value)
        return output
 
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, temperature=1.0):
        super().__init__()
        self.temperature  = temperature
 
    def forward(self, query, key, value, inv_scale):
        # scaled dot product of input tensor with key tensor.
        scaled_dot_product  = torch.matmul(query, key.transpose(-2,-1)) / inv_scale
 
        # softmax along the last dimension (the dimension corresponding to the temperature) 
        attention_weights    = self._softmax(scaled_dot_product, dim=-1)
        output               = attention_weights.matmul(value)
        return output
 
    def _softmax(self, x):
        