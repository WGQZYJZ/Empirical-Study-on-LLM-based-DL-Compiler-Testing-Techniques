
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, d_model=512):
        super().__init__()
 
        self.d_k = torch.nn.Parameter(
            torch.rand((384,), 1))
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query,
                                          key.transpose(-2, -1)) / (torch.norm(key) +
                                                                      self.d_k)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  =  attention_weights @ value
        return output


# Initializing the model
m1  = ScaledDotProductAttention()
m2  = ScaledDotProductAttention(4096)

# Inputs to the model
q  = torch.randn(384, 512)
k  = torch.randn(384, 512)
v  = torch.randn(384, 512)

# Outputs of the model
__output_1__, __output_2__ = m1(q, k, v), m2(q, k, v)

