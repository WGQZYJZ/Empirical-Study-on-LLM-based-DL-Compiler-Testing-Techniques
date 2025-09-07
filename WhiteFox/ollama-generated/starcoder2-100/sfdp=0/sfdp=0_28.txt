
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config):
        super().__init__()

        self.config = config
        
        self.softmax = torch.nn.Softmax(dim=-1)

    @staticmethod
    def _scaled_dot_product(query: torch.Tensor, key: torch.Tensor):
        dot_products  = query @ key.transpose(-2,-1).contiguous() # [batch size * sequence length, dim, dim]
        inv_scale = float(key.shape[-1]) ** -0.5
        return dot_products / inv_scale
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        attention_weights  = ScaledDotProductAttention._scaled_dot_product(query, key)

        scaled_attention_weights = self.softmax(attention_weights).expand(-1,-1,*value.shape[-2:]) # [batch size * sequence length, dim, *value dims]
        
        output  = torch.einsum('ij...,jk...->ik...', scaled_attention_weights, value) # [batch size * sequence length, dim, *value dims]

        return output

class MultiHeadAttention(torch.nn.Module):
    def __init__(self, config: dict):
        super().__init__()
        
        self._output_dim = config['hidden_size']
        
        self._scale  = torch.Tensor([config['attn_scale']]) # [1]
 
        self.query_proj  = torch.nn.Linear(in_features=config['hidden_size'], out_features=self._output_dim, bias=True)
        self.key_proj  = torch.nn.Linear(in_features=config['hidden_size'], out_features=self._output_dim, bias=True)

        self.dropout1 = torch.nn.Dropout(0.3, inplace=False)
        self.layernorm1 = LayerNorm(self._output_dim).to(torch.device('cuda'))

        self.dropout2 = torch.nn.Dropout(0.5, inplace=False)
        self.layernorm2 = LayerNorm(self._output_dim).to(torch.device('cuda'))
        
        self._scaled_dot_attention  = ScaledDotProductAttention(self._scale)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        v1 = self.query_proj(query)
        v2 = self.key_proj(key)
        v3 = torch.cat([v1, v2], -1)

        v4  = self._scaled_dot_attention(v3, key=self.key_proj(value), value=torch.nn.functional.gelu(v3))
        v5  = self.dropout1(v4)
 
        v6  = self.layernorm1(query + v5)

        v7  = self.dropout2(torch.nn.functional.gelu(self._output_dim, v6)) # gelu is the scaled GELU
        v8  = self.layernorm2(v6 + v7)
        return v8
