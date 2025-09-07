
class Model(torch.nn.Module):
    def __init__(self, embed_dim=1024, num_heads=8):
        super().__init__()
        self.multihead_attn = torch.nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)

    def forward(self, x1, key, value, inv_scale):
        scaled_dot_product  = torch.matmul(x1, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 1024, 64, 64)
key = torch.randn(1, 1024, 32, 32)
value = torch.randn(1, 1024, 64, 64)
inv_scale = 1/math.sqrt(128 * 32 * 64 + 64 * 1024)
