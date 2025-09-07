
class Attention(nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
            # Compute scaled dot-product attention
            inv_scale  = math.sqrt(query.shape[-1])
            scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
            attention_weights  = scaled_dot_product.softmax(dim=-1)
            # Compute the final output of the attention mechanism by multiplying the value with the attention weights and taking a weighted sum over the values
            attention  = attention_weights.matmul(value)
            return attention


class TransformerModel(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
 
        self.layers  = nn.Sequential(*[DecoderLayer(config=config) for _ in range(1)])
 
    def forward(self, x):
        return self.layers(x).softmax(-2)


class DecoderLayer(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
 
        self._norm1  = nn.LayerNorm(config.hidden_size)
        self._attn   = Attention()
        self._norm2  = nn.LayerNorm(config.hidden_size)
 
    def forward(self, x: torch.Tensor) -> torch.Tensor:
         out  = self._norm1(x + self._attn(query=x, key=x, value=x))
         return self._norm2(out), out
