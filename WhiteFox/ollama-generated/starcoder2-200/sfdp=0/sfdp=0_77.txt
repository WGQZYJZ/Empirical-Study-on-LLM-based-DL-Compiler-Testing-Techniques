
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v, inv_scale=100**-6):
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / inv_scale # 16 5 8 4
        attention_weights  = scaled_dot_product.softmax(dim=-1) 
        output  = attention_weights.matmul(v) 
        return output

# Initializing the model
m  = ScaledDotProductAttention()


# Inputs to the model
inv_scale=torch.randn((4,))
v = torch.randn(8, 256, 10000)
k = torch.randn(8, 256, 779339)
q = torch.randn(8, 256, 11)

 __output__  = m(q, k, v, inv_scale)
 