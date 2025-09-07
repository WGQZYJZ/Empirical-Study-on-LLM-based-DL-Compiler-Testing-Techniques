
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale):
        v1  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(key.size[-1])
        v3  = v1.softmax(dim=-1)
        v4  = v3.matmul(value)
        return v4


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = ScaledDotProductAttention()
 
    def forward(self, query, key, value, scale):
        v2  = self.attn_layer(query, key, value, scale)
 
        return v2


# Initializing the model
m  = Model()
 
__output__  = m(x1, x3, x4, 0.5987596)
