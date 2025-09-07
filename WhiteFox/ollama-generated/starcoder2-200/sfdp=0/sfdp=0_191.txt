
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=768):
        super().__init__()
 
        self.scale = torch.rsqrt(torch.tensor([dim], dtype=torch.float))
 
    def forward(self, query, key, value):
        # Scaled dot product attention
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


m1  = ScaledDotProductAttention() # Model object
__output__  = m1(torch.randn(2, 50, 768), torch.randn(2, 50, 768), torch.randn(2, 50, 768))

