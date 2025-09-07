
class Model(torch.nn.Module):
    def __init__(self, dim=128):
        super().__init__()
        self.dim = dim
 
    def forward(self, qkv):
        d_k = self.dim // 3 # depth per head
        h, w = qkv.shape[-2:]
        q, k, v = qkv.chunk(3, dim=-1)
        q *= math.sqrt(d_k)
        
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / d_k ** 0.5

        attention_weights = scaled_dot_product.softmax(dim=-1)

        output = attention_weights.matmul(v)
        return output
# Initializing the model
m = Model()

 # Inputs to the model
qkv = torch.randn(3, 64, 256, 8)
