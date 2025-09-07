
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.shape[-1])
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
 
        return output
 
m  = ScaledDotProductAttention()


# Inputs to the model
q  = torch.randn(32, 512)
k  = torch.randn(32, 512)
v  = torch.randn(32, 640)
__output__  = m(q, k, v)

