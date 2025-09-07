
class ScaledDotProductAttention(nn.Module):
    def __init__(self, dim, dropout):
        super().__init__()
        self.dropout = nn.Dropout2d(dropout)

        # Initialize a new 2D weight matrix of shape [batch_size, max_seq_len, num_attention_heads * head_dim]
        weight = torch.nn.Parameter(torch.randn(1, dim, dim))
        self.scale = nn.functional.softmax(weight, dim=-1)

        # We will set it to zero here for all heads in the first layer of ScaledDotProductAttention.
        self.reset_parameters()

    def reset_parameters(self):
        stdv = 1 / math.sqrt(self.scale.size(-1))
        return self.scale.data.uniform_(-stdv, stdv) * stdv
        # Weight initialization for ScaledDotProductAttention is done by the user in __init__()

    def forward(self, x, key, value, mask=None):
        if mask is not None:
            raise NotImplementedError('Masked ScaledDotProductAttention is not supported.')

        batch_size = x.shape[0]
        dim = x.shape[-1] // 2  # The number of attention heads in the scaled dot product attention mechanism.
        num_heads = self.scale.shape[1] // 2  # Number of heads in the scaled dot product attention.

        # Scaled Dot-Product Convolution to compute the attention weights.
        v, k, q = value.chunk(3, dim)
        v, k, q = v.contiguous().view(-1, dim), k.contiguous().view(-1, dim), q.contiguous().view(-1, dim)

        # Scale the query and key.
        scaled_dot_product = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(dim)
        scaled_dot_product = self.dropout(scaled_dot_product).view(batch_size, q.shape[0], num_heads, dim)

        # Compute the attention weights.
        attention_weights = torch.matmul(scaled_dot_product, self.scale)

        # Softmax on the weights to get the final output weights.
        attention_weights = nn.functional.softmax(attention_weights, dim=-1)

        # This step is optional for ScaledDotProductAttention.
        x = torch.matmul(attention_weights, v)  # X = alpha * (Q.T @ K) + beta
        return x


# Initializing the model
m = ScaledDotProductAttention(dim=8, dropout=0.1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key = torch.randn(1, 8, 8)
value = torch.randn(1, 8, 64, 64)
