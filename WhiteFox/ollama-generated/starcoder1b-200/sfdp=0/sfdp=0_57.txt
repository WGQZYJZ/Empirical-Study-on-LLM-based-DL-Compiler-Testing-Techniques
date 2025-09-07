
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim=-1):
        super().__init__()
        self.scale = 1.0 / np.sqrt(dim)

    def forward(self, x1, x2):
        # dot_product = torch.matmul(x1, x2).abs()
        # scaled_dot_product = dot_product * (inv_scale/np.sqrt(dot_product.size(-1)))
        inv_scale = self.scale / np.sqrt(x1.size(dim))
        scaled_dot_product = torch.matmul(x1, x2).abs() * inv_scale

        attention_weights = torch.softmax(scaled_dot_product, dim=-1)
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m  = ScaledDotProductAttention()


# Inputs to the model
q = torch.randn(4, 7, 30, 8)
k = torch.randn(4, 7, 8, 16)
v = torch.randn(4, 7, 8, 32)
