
class Model(torch.nn.Module):
    def __init__(self, n_heads, dim_q, dim_k, dim_v):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

        # Attention module
        self.attn = torch.nn.MultiheadAttention(dim_k=dim_k,
                                                dim_v=dim_v,
                                                num_heads=n_heads)
 
    def forward(self, x1):
        # Compute the input tensor for attention with size of (batch_size, seq_len, 8, feature_num, height, width)
        attn = self.attn(query=x1, key=None, value=None)[0]

        # Apply non-linearity
        output = self.conv(attn)

        return output


# Initializing the model
m = Model(n_heads=8, dim_q=64, dim_k=64, dim_v=64)

# Inputs to the model
x1 = torch.randn(32, 8, 128, 128)
