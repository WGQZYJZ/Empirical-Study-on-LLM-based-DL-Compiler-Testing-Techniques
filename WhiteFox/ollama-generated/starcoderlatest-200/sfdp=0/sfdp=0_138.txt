
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 16)
 
    def forward(self, q1, k1, v1):
        scaled_dot_product = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(v1.size(-1))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(2, 16, 32, 64)
k1 = torch.randn(8, 16, 32, 64)
v1 = torch.randn(8, 16, 32, 64)
