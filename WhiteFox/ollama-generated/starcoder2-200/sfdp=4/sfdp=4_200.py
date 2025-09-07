class MultiHeadAttention(torch.nn.Module):
    def __init__(self, hidden_size: int=128) -> None:
        super().__init__()
        self._qkv_proj = torch.nn.Linear(hidden_size, 3 * hidden_size)
        self._norm = torch.nn.LayerNorm(hidden_size)

    def forward(self, query: torch.Tensor, key: torch.Tensor, attn_mask=None):
        hidden_size = query.shape[-1]
        # Compute the dot product of the query and key tensors.
        # Multiply by a small value to avoid numerical issues
        # that could occur when performing a softmax over very large values.
        qkv = self._qkv_proj(query)  # Shape: [batch, head, seq-len, 3 * hidden]
        q, k, v = torch.chunk(qkv, chunks=3, dim=-1)

        qk = q @ k.transpose(-2, -1) / math.sqrt(hidden_size)
        if attn_mask is not None:
            qk += attn_mask  # Shape [batch, head, query-len, key-len]

        attn_weight = torch.softmax(qk, dim=-1)
        output = attn_weight @ v

        return self._norm(output + query)
