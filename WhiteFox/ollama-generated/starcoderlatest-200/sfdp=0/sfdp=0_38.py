
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, value, key, inv_scale=None):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale  # [B, H, N, M] * [N, M, H, K] -> [B, H, N, K]
        attention_weights  = scaled_dot_product.softmax(dim=-1)  # [B, H, N, K]
        output = attention_weights.matmul(value)  # [B, H, N, M] * [B, H, N, M] -> [B, H, N, M]
        return output


# Initializing the model
attn = ScaledDotProductAttention()


# Inputs to the model
query = torch.randn(1, 8, 64, 64)
value = torch.randn(1, 8, 64, 64)
key = torch.randn(1, 8, 64, 64)
scaled_dot_product = attn(query, value, key)
