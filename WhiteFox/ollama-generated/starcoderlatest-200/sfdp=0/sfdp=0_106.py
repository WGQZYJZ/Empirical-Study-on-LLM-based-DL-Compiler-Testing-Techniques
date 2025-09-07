
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, q, k, v):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.size(-1))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output

# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(5, 3, 64, 64)
k  = torch.randn(5, 8, 64, 64)
v  = torch.randn(5, 8, 64, 64)
