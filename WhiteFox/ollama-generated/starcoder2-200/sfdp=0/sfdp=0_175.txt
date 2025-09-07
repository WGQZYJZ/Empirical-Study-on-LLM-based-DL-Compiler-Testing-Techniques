
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1: torch.Tensor, k1: torch.Tensor, v1: torch.Tensor) -> torch.Tensor:
        # Shape of `q`, `k`, and `v` is [batch_size, num_heads, length_query/key, depth]
        batch_size = q1.shape[0]
        num_heads = q1.shape[1]
 
        inv_scale = torch.pow(torch.tensor(768), -0.5)  # Inverse scaling factor to stabilize the gradients
        scaled_dot_product = torch.matmul(q1 / inv_scale, k1 / inv_scale)  # Scaled dot product
        
        # Shape of `scaled_dot_product` is [batch_size, num_heads, length_query/key, length_value]

        attention_weights = scaled_dot_product.softmax(dim=-2)
        # Shape of `attention_weights` is [batch_size, num_heads, length_query, length_key]
 
        output  = torch.matmul(attention_weights, v1)
        # Shape of `output` is [batch_size, num_heads, length_value, depth]

        return output


