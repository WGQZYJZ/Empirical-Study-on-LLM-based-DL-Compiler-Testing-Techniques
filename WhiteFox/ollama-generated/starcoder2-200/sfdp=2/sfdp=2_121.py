

class SelfAttention(nn.Module):
    def __init__(self, dim: int = 512, num_heads: int = 8) -> None:
        super().__init__()

        self._dim = dim
        self._num_heads = num_heads

        # Compute the dimensionality of each head based on the total dimensionality.
        self._head_dim = self._dim // self._num_heads

        assert self._head_dim * self._num_heads == self._dim, "Total dimension should be divisible by number of heads."
        self._scale_factor = math.sqrt(self._head_dim)  # Scale factor

        self._query = nn.Linear(dim, dim, bias=False)
        self._key = nn.Linear(dim, dim, bias=False)
        self._value = nn.Linear(dim, dim, bias=False)

    def forward(self, hidden_states: torch.Tensor) -> torch.Tensor:

        # Reshape the hidden states into a 3D tensor of query, key and value.
        query = self._query(hidden_states).reshape(
            -1, self._num_heads, self._head_dim
        )
        key = self._key(hidden_states).reshape(
            -1, self._num_heads, self._head_dim
        )

        # Scale the dot product by an inverse scale factor.
        scaled_query = torch.div(query, self._scale_factor)

        # Compute the dot product of the query and key.
        qk = scaled_query @ key.transpose(-2, -1).contiguous()

        # Apply softmax on the scaled dot product.
        attention_weights = nn.Softmax(dim=-1)(qk)

        # Apply dropout to the output of softmax (not to qk!).
        dropout_qk = nn.Dropout(dropout_p)(attention_weights)

        # Compute the dot product of the dropout and value matrices.
        return dropout_qk @ self._value(hidden_states).reshape(-1, self._dim), attention_weights


m  = SelfAttention()
__output__  = m(torch.randn(32,512))



