
class Model(torch.nn.Module):
    def __init__(self, dim_k, dim_v, num_heads=1):
        super().__init__()
        self.dim_k = dim_k
        self.dim_v = dim_v
        self.num_heads = num_heads
        
        self.scale  = math.sqrt(dim_k / (dim_k + dim_v))
        
        # Note: The output of a pointwise convolution is multiplied by a constant `0.5`.
        self.multihead_attn = MultiHeadAttention(dim_k, dim_v, num_heads)

    def forward(self, query, key, value):
        attn_weight, _ = self.multihead_attn(query, key, value)
        return attn_weight @ value


# Initializing the model
m = Model(dim_k=64, dim_v=128)

# Inputs to the model
query  = torch.randn(4, 3, 64, 64)
key     = torch.randn(4, 5, 64, 64)
value   = torch.randn(4, 6, 64, 128)
