
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
 
    def forward(self, q1, k1, v1):
        inv_scale = (q1**2).sum(-1, keepdim=True) * (k1**2).sum(-2, keepdim=True).sqrt().reciprocal()
        scaled_dot_product = torch.matmul(q1, k1.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
 
        # ScaledDotProductAttention block with dimension of the key and query vectors
        # Note that this module is different from the class defined in AttentionBlock above: here the scaling factor is not used (inv_scale). 
        sddp = ScaledDotProductAttention(dim=self.conv.out_channels)
 
        output = sddp(q1, k1, v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
