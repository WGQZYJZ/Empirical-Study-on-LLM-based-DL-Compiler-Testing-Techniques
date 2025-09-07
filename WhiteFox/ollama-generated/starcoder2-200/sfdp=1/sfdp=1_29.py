class MultiHeadedAttentionModel(torch.nn.Module):
    def __init__(self, head_count: int) -> None:
        super().__init__()
        self._head_count = head_count
        self._head_dim = 1024 // head_count
 
    def forward(self,
                query: torch.Tensor, 
                key: torch.Tensor,
                value: torch.Tensor,) -> torch.Tensor: 
        scale_factor = float(torch.rsqrt(torch.tensor([self._head_dim])))
        inv_scale  = -1 * self._head_count * scale_factor ** 2
        # Compute the dot product of query and key, then scale it by inverse scale factor, apply softmax and dropout
        v = torch.nn.functional.softmax(torch.div(
            torch.matmul(query, key.transpose(-2, -1)).mul(inv_scale), 
            inv_scale
        ), dim=-1).mul(dropout)
        # Compute the dot product of the scaled output and value tensor
        return v.matmul(value)


model  = MultiHeadedAttentionModel()
inputs  = (torch.randn(5, 32768), torch.randn(5, 32768), torch.randn(5, 1024))
outputs  = model(*inputs)
