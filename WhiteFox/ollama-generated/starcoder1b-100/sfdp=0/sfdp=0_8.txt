
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, temperature: float = 1.0):
        super().__init__()
        self.temperature = temperature

    def forward(self, query, key, value, mask=None):
        batch_size, seq_len = query.shape
        scale_x = torch.div(torch.norm(query, dim=-1),
                             torch.sqrt(seq_len + self.temperature))

        scale_y = torch.div(torch.norm(key, dim=-1),
                             torch.sqrt(seq_len + self.temperature))

        dot_product = torch.matmul(scale_x, key) / scale_y

        mask_select = torch.mul(dot_product, value.unsqueeze(-2).expand(batch_size, seq_len, -1)).sum(dim=2)
        weights = mask_select / (self.temperature * mask_select.sum(dim=2))

        output = weights.matmul(value)

        return output


# Initializing the model
m  = ScaledDotProductAttention()


