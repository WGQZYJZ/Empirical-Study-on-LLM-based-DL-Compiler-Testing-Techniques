import torch
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.scale = 1 / (dim ** 0.5)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) * self.scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)

        return output
