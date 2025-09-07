
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=1e-6) -> None:
        super().__init__()
        self._inv_scale  = inv_scale
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / self._inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output

class TransformerBlock(torch.nn.Module):
    def __init__(self, num_attention_heads: int=8, dim: int=500, inv_scale=4096., attn_dropout=0.1, residual_dropout=0.1) -> None:
        super().__init__()
 
        self._linear = torch.nn.Linear(dim, num_attention_heads * 2 * dim // num_attention_heads + 50)
        self._attn  = ScaledDotProductAttention(inv_scale)
 
    def forward(self, input1: torch.Tensor):
        query  = torch.nn.functional.normalize(input1).transpose(-2, -1)
        key   = torch.nn.functional.normalize(query).transpose(-2, -1)
        value  = query
 
        attention_output  = self._attn(query=query, key=key, value=value) + input1
 
        output  = self._linear(attention_output) + self._dropout(self._residual_dropout(input))

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self._transformer_block = TransformerBlock()
 
    def forward(self, input1: torch.Tensor):
        return self._transformer_block(input)

# Initializing the model
m  = Model()
 
# Inputs to the model
inputs  = torch.randn(304962, 50)
 
 __output__  = m(inputs)
