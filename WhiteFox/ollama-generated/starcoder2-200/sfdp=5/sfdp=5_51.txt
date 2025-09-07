
class Model(torch.nn.Module):
    def __init__(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        super().__init__()

    def forward(self, attn_mask=None) -> torch.Tensor:  # noqa: D102
        vq = self.query @ self.key.transpose(-2, -1) / math.sqrt(self.query.size(-1))
        if attn_mask is not None and not self._masked_indices() == 0
            vq += attn_mask

        return torch.softmax(vq, dim=-1), torch.dropout(vq + attn_mask, dropout_p=0.2) @ self.value


# Initializing the model