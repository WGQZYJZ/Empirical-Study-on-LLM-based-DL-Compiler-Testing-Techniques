
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, temperature):
        super().__init__()
        self.temperature = temperature
 
    def forward(self, q, k, v):
        attn = torch.matmul(q / self.temperature, k.transpose(-2, -1)) / math.sqrt(k.shape[-1])
        return attn

class Model(torch.nn.Module):
    def __init__(self, temperature=1000.):
        super().__init__()
        self.scaled_dot_product_attention = ScaledDotProductAttention(temperature)
 
    def forward(self, q, k, v):
        attn = self.scaled_dot_product_attention(q, k, v)
        return torch.matmul(attn, v), None

# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1, 3, 64, 64)
key    = torch.randn(1, 3, 64, 64)
value  = torch.randn(1, 3, 64, 64)
__output__ , __unused__ = m(query, key, value)


