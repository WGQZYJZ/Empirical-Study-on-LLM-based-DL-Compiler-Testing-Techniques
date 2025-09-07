
class Attention(torch.nn.Module):
    def __init__(self, feature_dim, num_heads=8):
        super().__init__()
        self.feature_dim = feature_dim
        self.num_heads = num_heads
        self.linear_q = torch.nn.Linear(feature_dim, num_heads * 3) # TODO: The number of output features is 64 x 8 x 4 x 4 = 1280 for now. In practice this may be reduced to something like 512 or 128
        self.linear_k = torch.nn.Linear(feature_dim, num_heads * 3) # TODO: The number of output features is 64 x 8 x 4 x 4 = 1280 for now. In practice this may be reduced to something like 512 or 128
        self.linear_v = torch.nn.Linear(feature_dim, num_heads * 3) # TODO: The number of output features is 64 x 8 x 4 x 4 = 1280 for now. In practice this may be reduced to something like 512 or 128

    def forward(self, q, k, v):
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value) # TODO: Replace "output" with attention_weights
        return output

# Initializing the model
attention = Attention()
m = TransformerBlock(attention)


# Inputs to the model
x1 = torch.randn(1, 64, 32, 32)
x2 = torch.randn(1, 64, 32, 32)
