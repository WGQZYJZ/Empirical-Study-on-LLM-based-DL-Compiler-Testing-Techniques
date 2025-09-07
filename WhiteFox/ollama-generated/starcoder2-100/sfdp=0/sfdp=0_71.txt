
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, mask: torch.BoolTensor = None) -> torch.Tensor:
        # Compute the scaled dot product and apply the softmax function to it using `dim=-1`
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size()[-1])
 
        if mask is not None:
            scaled_dot_product[mask == False]  = -math.inf
 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights @ value
        return output


