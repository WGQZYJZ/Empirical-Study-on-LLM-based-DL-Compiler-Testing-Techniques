
class ScaledDotProductAttention(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale=None):
        # Scale the matrix for numerical stability.
        scale = torch.max(scale if scale is not None else torch.tensor(1e-6),
                          torch.min(torch.abs(query), torch.abs(key)))
        scale = 1 / scale
        query_norm = query @ key.transpose(-2, -1) * scale
        key_norm = (key @ key.transpose(-2, -1)) * scale

        # Multiply by the attention weights.
        dot_product = torch.matmul(query_norm, key_norm)

        # Apply softmax to get the attention weights.
        att = nn.Softmax(dim=-1)(dot_product)  # Shape: [B, T]
        return (att @ value).transpose(-2, -1)


# Initializing the model
m = ScaledDotProductAttention()

