
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        
        # Compute the scaled dot product attention for a given query, key and value tensor
        inv_scale = torch.tensor(float(key.shape[-1])).sqrt()

        scaled_dot_product  =  torch.matmul(query,  key.transpose(-2, -1)) /  float(inv_scale)
        attention_weights  =  scaled_dot_product .softmax(dim=-1)
        output  =  attention_weights.matmul(value)

        return output
# Initializing the model