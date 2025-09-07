
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim_head: int, inv_scale=None):
        super().__init__()
        self.dim_head = dim_head
        self.inv_scale = inv_scale
 
    def forward(self, query, key, value, attn_mask=None):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / (self.inv_scale if self.inv_scale is not None else query.shape[-1] ** 0.5)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output             = attention_weights.matmul(value)
        return output
 

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        dim_head   = 64
        conv       = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        conv_mask  = torch.nn.Conv2d(2, 8, 1, stride=1, padding=1)
 
        self.attn = ScaledDotProductAttention(dim_head)
        self.conv_q = conv
        self.conv_k = conv
        self.conv_v = conv
        self.conv_mask = conv_mask
 
    def forward(self, x):
        # 1. The output of the convolution is used to compute the attention weights.
        q = self.conv_q(x)
        k = self.conv_k(x)
        v = self.conv_v(x)
 
        q *= torch.sigmoid(self.conv_mask(x[:, :2].transpose(-2, -1)))
 
        # 2. The attention weights are used to compute the weighted sum of the value tensor.
        out = self.attn(q, k, v)
        return out
 

# Initializing the model
m = Model()


# Inputs to the model
x_attn = torch.randn(1, 3, 64, 64)
