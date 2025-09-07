
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, scale=1.0, dropout=0.0):
        super().__init__()
        self.dropout = nn.Dropout2d(dropout)
        self.scale = scale

    def forward(self, query, key, value, mask):
        if not mask is None:
            return self._masked_scaled_dot_product_attention(query=query,
                                                           key=key,
                                                           value=value,
                                                           mask=mask)
        else:
            return self._unmasked_scaled_dot_product_attention(query=query,
                                                              key=key,
                                                              value=value)

    def _masked_scaled_dot_product_attention(self, query, key, value,
                                               mask):
        batch_size = query.shape[0]
        dim = query.dim() - 1

        # Compute the mask for the last dimension
        if mask is None:
            mask = torch.triu(
                torch.ones((batch_size, batch_size),
                         device=query.device) * float('-inf'),
                1)
            mask = mask.triu(diagonal=-1).transpose(-2, -1)  # (b, b, c, h, w)
            mask = self.dropout(mask)

        # Compute the dot-product mask
        query_norm = query / math.sqrt(query.shape[dim])
        key_norm   = key / math.sqrt(key.shape[dim])
        attn_weights = (query_norm @ key_norm.transpose(-2, -1))  # (b, h, w) / sqrt(h)

        # Apply the dot-product mask and scale
        scaled_dot_product = query_norm @ key_norm.transpose(-2, -1).masked_fill_(
            ~mask, float('-inf'))
        return attn_weights * self.scale * torch.exp(scaled_dot_product)

    def _unmasked_scaled_dot_product_attention(self, query, key, value):
        batch_size = query.shape[0]

        # Compute the norms of the query and key tensors
        query_norm = query / math.sqrt(query.shape[1])
        key_norm   = key / math.sqrt(key.shape[1])

        # Compute the dot-product mask and scale
        scaled_dot_product = query_norm @ key_norm.transpose(-2, -1)
        return torch.exp(scaled_dot_product) * self.scale


# Initializing the model
m  = ScaledDotProductAttention()

