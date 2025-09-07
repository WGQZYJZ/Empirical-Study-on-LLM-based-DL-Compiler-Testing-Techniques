
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mha = torch.nn.MultiheadAttention(dim_q=128, dim_k=128, num_heads=16)
 
    def forward(self, q, k, v):
        scaled_dot_product = self.mha(q, k, v)[0]
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v)
        return output

# Inputs to the model
q  = torch.randn(256, 32, 128)
k  = torch.randn(256, 32, 128)
v  = torch.randn(256, 32, 128)
