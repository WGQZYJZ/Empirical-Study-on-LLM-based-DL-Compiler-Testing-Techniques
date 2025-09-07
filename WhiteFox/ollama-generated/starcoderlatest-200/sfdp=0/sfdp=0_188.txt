
class Model(torch.nn.Module):
    def __init__(self, num_heads=128, attention_resolutions=(64, 32)):
        super().__init__()
        self.attention = ScaledDotProductAttention(
            dim = query.shape[-1], 
            num_heads = num_heads, 
            resolution = attention_resolution)
 
    def forward(self, q, k, v):
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(k.shape[-1])
        attention_weights  = self.attention(scaled_dot_product, q, key)
        output = attention_weights.matmul(v)
        return output
 
# Initializing the model
m = Model(num_heads=128, attention_resolutions=(64, 32))

 # Inputs to the model
    query  = torch.randn(1, 256, 64, 64)
    key    = torch.randn(1, 1024, 64, 64)
    value  = torch.randn(1, 2048, 64, 64)
