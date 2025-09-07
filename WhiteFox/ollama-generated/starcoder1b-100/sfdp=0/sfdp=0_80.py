
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, head_dim=None):
        super().__init__()
        self.head_dim = head_dim
        if head_dim is None:
            self.scale = 1 / math.sqrt(torch.FloatTensor([m[0].shape[0] for m in (query, key)]))

    def forward(self, query, key, value, mask=None):
        # Compute the dot product of the input and output tensor to get the attention weights:
        qkv = torch.matmul(query, key.transpose(-2, -1)) / self.scale  # Shape is (batch_size, seq_len_q * heads, hidden_dim)
        if mask is not None:
            return torch.masked_softmax(qkv, mask=mask, dim=-1) * value
        else:
            return torch.softmax(qkv, dim=-1) * value


# Initializing the model
scaled_dot_product = ScaledDotProductAttention()


