
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q, k, v): # v is always equal to value in the implementation
        dim_key, dim_query, dim_value = q.size(-2), q.size(-1), k.size(-2)
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(dim_key)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(v)
        return output


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        dot_product  = torch.matmul(q1, k1.transpose(-2, -1))
        attention_weights = dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(v1)
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(4096, 3, 16, 8)
q1 = torch.randn(1, 128, 1, 1) # q1 is always equal to query in the implementation
