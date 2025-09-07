
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention()
 
    def forward(self, query, key, value):
        v6 = self.attn(query, key, value)
        return v6


# Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(32, 5, 8, 8)
k1 = torch.randn(32, 5, 4, 4)
v1 = torch.randn(32, 5, 32, 32)
 
