
class ScaledDotProductAttention(nn.Module):
    def __init__(self, d_k=None, d_v=None, scale=None, dropout=None, max_len=1024):
        super().__init__()
        self.scale = nn.Parameter(torch.tensor(scale))
        self.dropout = nn.Dropout(dropout)
        if d_k is not None and d_v is not None:
            self.query = Linear(d_k, scale * d_k)
            self.key = Linear(d_v, scale * d_v)
        elif d_k is not None:
            self.query = Linear(d_k, scale * d_k)
        elif d_v is not None:
            self.key = Linear(d_v, scale * d_v)

    def forward(self, x, attn_mask):
        # Shape: batch_size x n_heads x sequence_length_1 x sequence_length_2 x dim
        n_batches = attn_mask.shape[0]

        query = self.query(x).view(n_batches, -1, *x.shape[-3:])  # (batch_size x n_heads x sequence_length_1 x dim)
        key = self.key(x).view(n_batches, -1, *x.shape[-3:])  # (batch_size x n_heads x sequence_length_2 x dim)

        # Shape: batch_size x n_heads x n_sequence_length_1 x n_sequence_length_2 x scale
        scaled_dot_product = torch.einsum('bhij,bhki->bhi', query, key).view(n_batches, -1, attn_mask.shape[1]) * self.scale

        # Shape: batch_size x sequence_length_1 x sequence_length_2
        mask = attn_mask.float()  # (batch_size x n_heads x sequence_length_1 x sequence_length_2)

        # Shape: batch_size x n_heads x sequence_length_1 x sequence_length_2
        attention_weights = scaled_dot_product.softmax(dim=-1) * mask

        # Shape: batch_size x sequence_length_1 x sequence_length_2
        attention = attention_weights.matmul(x)

        # Shape: batch_size x sequence_length_1 x sequence_length_2
        output = self.dropout(attention + x).view(n_batches, -1, *x.shape[-3:])  # (batch_size x sequence_length_1 x sequence_length_2)

        return output


# Initializing the model
m = ScaledDotProductAttention()


