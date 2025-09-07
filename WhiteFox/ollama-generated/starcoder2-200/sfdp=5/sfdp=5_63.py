
class Attention(torch.nn.Module):
    def __init__(self, dropout=0.1):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, attn_mask = None) -> torch.Tensor: 
        v1  = self._apply_scaled_dot_product_attention(query, key)
        if not attn_mask is None and not torch.isfinite(attn_mask):
            v2 = v1 * -1e9
        else:
            v2 = v1
        return v2
    
    def _apply_scaled_dot_product_attention(self, query: torch.Tensor, key: torch.Tensor) -> torch.Tensor:
        qk  = query @ key.transpose(-2,-1)/ math.sqrt(query.size(-1))
        if not attn_mask is None and not torch.isfinite(attn_mask):
            v3  = qk + attn_mask
        else:
            v3  = qk 
        return self._apply_dropout_on_attention_weights(v3)
    
    def _apply_dropout_on_attention_weights(self, weighted_values : torch.Tensor ) -> torch.Tensor:
         v4  = weighted_values * dropout
        return v4

m  = Attention()

 # Inputs to the model
__inputs__ = {
    'query': torch.randn(10, 20), 
    'key'  : torch.randn(30, 5)
}

 # Initializing the model with arguments
 m(**__inputs__) 
