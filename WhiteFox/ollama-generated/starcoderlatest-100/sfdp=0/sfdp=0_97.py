
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v):
        inv_scale = torch.rsqrt(torch.tensor(k.shape[-1]))
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) * inv_scale
        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
        output = attention_weights.matmul(v)
        return output
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, q, k, v):
        attention = self.attention(q, k, v)
        return attention
 
 # Initializing the model
m = Model()
 
 # Inputs to the model
q = torch.randn(256, 16, 4, 4)
k = torch.randn(128, 32, 5, 5)
v = torch.randn(256, 128, 4, 4)
 
 # Expected output: Tensor containing the attention weights (before softmax)
