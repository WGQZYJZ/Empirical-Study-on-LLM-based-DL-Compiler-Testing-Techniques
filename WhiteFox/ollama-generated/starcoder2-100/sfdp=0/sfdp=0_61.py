
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, scale=None):
         if scale is not None:
            scale = scale * (q.size(-1)**-0.5)
         scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(v)
        return output


# Initializing the model
m  = ScaledDotProductAttention()
 
# Input tensors to the model
query, key, value = torch.randn(2048, 512), torch.randn(2048, 512), torch.randn(2048, 512)


# Inputs to the model
q_1, k_1, v_1, scale_1 = query, key, value, 768**-0.5
 
__output__  = m(q_1, k_1, v_1, scale=scale_1)

