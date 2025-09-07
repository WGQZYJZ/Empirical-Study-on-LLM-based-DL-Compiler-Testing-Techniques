
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale=None):
        if scale is None:
            inv_scale = torch.rsqrt(
                torch.pow(key.size()[-1], 0.5) / (torch.matmul(query, key.transpose(-2, -1)) + 1e-7)
            )
        else:
            inv_scale = scale
        return F.softmax(
            scaled_dot_product=torch.matmul(query, key.transpose(-2, -1)), dim=-1) * inv_scale


# Initializing the model
m = ScaledDotProductAttention()


