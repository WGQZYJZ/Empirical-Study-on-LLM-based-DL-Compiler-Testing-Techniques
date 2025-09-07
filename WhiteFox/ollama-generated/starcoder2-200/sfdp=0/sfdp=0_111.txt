
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.nn.Parameter(
            torch.ones(1) / (32 ** 0.5), requires_grad=False
        )
 
    def forward(self, query, key, value):
 
        # Additive self-attention without bias and no layer norm
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self.scale
        
        # Compute attention using the softmax
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        
        output  = attention_weights.matmul(value)
 
        return output


# Initializing the model