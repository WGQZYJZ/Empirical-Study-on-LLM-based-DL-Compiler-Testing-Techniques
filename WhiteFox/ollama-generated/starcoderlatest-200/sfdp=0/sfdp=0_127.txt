
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 8)
 
    def forward(self, q, k, v):
        attn_weights = self.attn(q, k, v)[0]
        scaled_dot_product = attn_weights * torch.rsqrt(torch.tensor(8)) 
        output = torch.matmul(scaled_dot_product, v)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 8, 512, 64)
k = torch.randn(1, 8, 512, 64)
v = torch.randn(1, 8, 512, 64)
