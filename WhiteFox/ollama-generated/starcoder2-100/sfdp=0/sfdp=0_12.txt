
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale: float = 1.) -> None
        super().__init__()
        self.inv_scale = torch.tensor(
            inv_scale).to(torch.get_default_device())
    
    def forward(self, query: Tensor, key: Tensor, value: Tensor) -> Tensor:
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self.inv_scale

        # Compute the softmax of the scaled dot product
        attention_weights = scaled_dot_product.softmax(dim=-1)
        
        output  = attention_weights @ value
        return output


model = ScaledDotProductAttention()
