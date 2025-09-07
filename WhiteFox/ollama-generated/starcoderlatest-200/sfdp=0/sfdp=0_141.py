
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, scale: float = None) -> (torch.Tensor, torch.Tensor):
        inv_scale = 1 / math.sqrt(query.size(-2)) if scale is None else scale
 
        att_logits = torch.matmul(query, key.transpose(-2, -1)) * inv_scale
        attention_weights = self.dropout(F.softmax(att_logits, dim=-1))
        output = torch.matmul(attention_weights, value)
        return output, attention_weights


class MultiHeadAttention(torch.nn.Module):
    def __init__(self, num_heads: int):
        super().__init__()
        self.num_heads = num_heads
 
        inner_dim  = query.size(-1) // num_heads
        head_dim   = inner_dim  * num_heads
 
        self.query    = torch.nn.Linear(head_dim, num_heads, bias=False)
        self.key      = torch.nn.Linear(head_dim, num_heads, bias=False)
        self.value    = torch.nn.Linear(head_dim, num_heads, bias=False)
 
        self.out_proj = torch.nn.Linear(num_heads * head_dim, inner_dim)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        q = self.query(query).view(-1, self.num_heads, -1)
        k = self.key(key).view(-1, self.num_heads, -1)
        v = self.value(value).view(-1, self.num_heads, -1)
 
        q = q * (self.num_heads ** 0.5)
        attention_output, attention_weights = ScaledDotProductAttention()(q, k, v)
        attention_output = attention_output.view(*query.size()[:-2], self.num_heads * head_dim)
 
        output = self.out_proj(attention_output)
        return output, attention_weights
 
# The final model should be different from the previous one and must satisfy the following pattern:
class Model(torch.nn.Module):
    def __init__(self, num_heads=4):
        super().__init__()
 
        self.layers = torch.nn.Sequential()
 
        for _ in range(num_heads):
            layer = torch.nn.Sequential(
                ScaledDotProductAttention(),
                torch.nn.LayerNorm(16),
                torch.nn.ReLU(),
            )
            self.layers.add_module("layer_%d" % _, layer)
 
    def forward(self, x):
        x = self.layers[0](x)
        for i in range(len(self.layers) - 1):
            if isinstance(self.layers[i], ScaledDotProductAttention):
                x, attn_weights = self.layers[i](x)
                if i == len(self.layers) - 2:
                    # Add attention weights to the last layer for visualization purposes
                    return x, attn_weights
        return x
 
# Initialization of the model and generate an input tensor
m = Model()
in_tensor  = torch.randn(32, 16, 7, 8)
