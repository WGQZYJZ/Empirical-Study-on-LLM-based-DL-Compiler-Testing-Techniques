
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, inv_scale=1.0):
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / (k.shape[-1] ** 0.5)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v).div_(inv_scale)
 
        return output

# Initializing the model
m = ScaledDotProductAttention()

 # Inputs to the model
q  = torch.randn(4, 8, 32)
k  = torch.randn(4, 8, 64).mul_(0.75).tanh().div_(0.1)
v  = torch.randn(4, 8, 128)

 # Inputs to the model
inv_scale  = k.shape[-1] ** 0.5
__output__  = m(q, k, v, inv_scale=inv_scale)
