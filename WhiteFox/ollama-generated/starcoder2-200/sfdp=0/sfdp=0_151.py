class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=1., trainable_scale=False) -> None:
        super().__init__()
        self._inv_scale = torch.nn.Parameter(inv_scale * torch.ones(()))
 
    @torch.no_grad()
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / self._inv_scale 
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        return attention_weights.matmul(value), 0


class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.sdp  = ScaledDotProductAttention()
 
    @torch.no_grad()
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> tuple[torch.Tensor]:
        v1,  v2 = self.sdp(query=query, key=key, value=value)
        return v1


# Initializing the model
m  = Model()
 
 # Inputs to the model
 query  = torch.randn(32,  64)
 key    = torch.randn(32, 512) 
 value  = torch.randn(32, 512)
 __output__  = m(query=query, key=key, value=value)

 
