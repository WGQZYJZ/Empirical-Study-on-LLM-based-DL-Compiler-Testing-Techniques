

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=1024):
        super().__init__()
        self._scale = torch.rsqrt(torch.tensor(float(dim), dtype=torch.float32))
 
    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) * self._scale 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
 
        return attention_weights.matmul(value), attention_weights


model = ScaledDotProductAttention()

 # Inputs to the model
q = torch.randn(800, 32, 512, requires_grad=True) * 0.1
k = torch.randn(800, 32, 512, requires_grad=True) * 0.1
v = torch.randn(800, 32, 512, requires_grad=True) * 0.1

 # Initializing the model
m(q, k, v), __output__

# Input tensors are randomly generated.
