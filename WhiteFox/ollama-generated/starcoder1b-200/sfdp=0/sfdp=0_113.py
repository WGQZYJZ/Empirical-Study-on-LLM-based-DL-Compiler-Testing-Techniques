
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim, scale=1e-6):
        super().__init__()
        self.dim = dim
        self.scale = torch.sqrt(torch.FloatTensor([scale]))

    def forward(self, q, k, v):
        dots = torch.matmul(q, k.transpose(-2, -1))
        inv_scale = 1 / (self.scale * torch.sqrt(torch.FloatTensor([self.dim])))

        attention_weights = dots.softmax(dim=-1)
        output = attention_weights.matmul(v)

        return output


# Initializing the model
scaled_dot_product_attention = ScaledDotProductAttention(256)


