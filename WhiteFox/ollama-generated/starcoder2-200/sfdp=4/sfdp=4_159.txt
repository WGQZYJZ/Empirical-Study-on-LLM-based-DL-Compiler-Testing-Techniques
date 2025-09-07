
class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, config: torch.Tensor):
        super().__init__()
 
        self.query  = torch.nn.Linear(config['d_model'], config['d_k'])
        self.key    = torch.nn.Linear(config['d_model'], config['d_k'])
        self.value  = torch.nn.Linear(config['d_model'], config['d_v'])
 
        self._mask   = torch.nn.Parameter(torch.Tensor([0]), requires_grad=False)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor):
        attn  = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) + self._mask[:, None]
        attn  = torch.softmax(attn, dim=-1)
 
        out   = attn @ value
        return out

# Initializing the model
model_1  = ScaledDotProductAttention({'d_model':32})
model_2  = ScaledDotProductAttention({'d_model':64,'d_k':8, 'd_v':8})

 # Inputs to the model.
query   = torch.randn(300, 128)
key     = torch.randn(300, 128)
value   = torch.randn(300, 64)
 
__output_1__  = model_1(query, key, value) # Attention weights
__output_2__  = model_2(query, key, value) # Attention weights
 
