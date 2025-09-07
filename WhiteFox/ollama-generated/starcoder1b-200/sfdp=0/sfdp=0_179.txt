
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, num_attention_heads):
        super().__init__()
        self.num_attention_heads = num_attention_heads
 
    def forward(self, query, key, value, mask=None):
        if mask is not None:
            batch_size = query.shape[0]
            mask = torch.tril(mask) + mask  # Add a little bit to avoid broadcasting.
            mask = mask.view(1, -1, self.num_attention_heads, self.num_attention_heads)
            padding_mask = (mask == float("-inf")).unsqueeze(-1)
        else:
            batch_size, seq_len, _ = query.shape
        # Perform matrix multiplication.
        score = torch.matmul(query, key) / math.sqrt(self.num_attention_heads * self.num_attention_heads + 0.00001)
 
        if mask is not None:
            padding_mask = padding_mask.unsqueeze(-1)
            attention_weights = score.masked_fill(padding_mask, float("-inf"))
        else:
            attention_weights = score.softmax(dim=-1)

        output = torch.matmul(attention_weights, value)
        return output


# Initializing the model
attn = ScaledDotProductAttention(8)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
