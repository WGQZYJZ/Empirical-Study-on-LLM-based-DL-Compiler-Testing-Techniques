
class AttentionModule(torch.nn.Module):
    def __init__(self, num_heads=4):
        super().__init__()
        self.num_heads = num_heads
 
    def forward(self, qk):
        ...
 
    @staticmethod
    def _shape(n, h):
        return (n, h, n // h)
 
    def get_attn_mask(self, key):
        ...
 
    @staticmethod
    def _expand(x):
        x1, x2 = torch.chunk(x, 2, dim=-3)
        return torch.cat((x1[:, :, None].repeat(1, 8, x2.shape[-1]),
                           x2[:, :, :, None].repeat(1, x1.shape[1], 1)), dim=-3)
 
    @staticmethod
    def _split(x, num_heads):
        x = torch.chunk(x, num_heads, dim=-2)
        return (x1, qk, key, value)


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    @staticmethod
    def _shape(n, h):
        return (n, h, n // h)
 
    @staticmethod
    def _expand(x):
        x1, x2 = torch.chunk(x, 2, dim=-3)
        return torch.cat((x1[:, :, None].repeat(1, 8, x2.shape[-1]),
                           x2[:, :, :, None].repeat(1, x1.shape[1], 1)), dim=-3)
 
    @staticmethod
    def _split(x, num_heads):
        x = torch.chunk(x, num_heads, dim=-2)
        return (x1, qk, key, value)
 
    def forward(self, x1):
        v1 = self.conv(x1)  # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 * 0.5  # Multiply the output of the convolution by 0.5
 
        qk = torch.matmul(v1[:, :, None, :].repeat(1, self.num_heads, 1, 1),
                           key) / math.sqrt(v1.size(-1))
        k = AttentionModule._split(qk, self.num_heads)[2]
 
        attn_weight = torch.softmax(qk * 0.5, dim=-1) # Apply softmax to the result
        output = torch.matmul(attn_weight[:, :, :, None].repeat(1, 1, 8, 1),
                              value)
 
        return output
 
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
