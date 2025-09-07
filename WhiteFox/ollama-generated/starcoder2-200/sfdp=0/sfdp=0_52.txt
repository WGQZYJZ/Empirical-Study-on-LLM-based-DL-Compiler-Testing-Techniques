
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config: dict) -> None:
        super().__init__()
        self._scale = 1 / math.sqrt(config['head_dim'])
 
    def forward(
            self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor
            ) -> Tuple[torch.Tensor]:
 
        attention = torch.matmul(query, key.transpose(-2, -1)) * self._scale
        # Compute the attention weights using the scaled dot product.
        # Apply softmax to normalize the probabilities of each head.
        attention_weights = F.softmax(
            attention, dim=-1)  # [batch_size x num_heads x seq_len_q x seq_len_k]
        output = torch.matmul(attention_weights, value)
        return output
