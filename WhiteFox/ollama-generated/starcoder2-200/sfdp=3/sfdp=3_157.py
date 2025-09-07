
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scale = 10.
        p = 0.5
        
        self_attention = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) * scale
        softmax_qk = self_attention.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=p)
 
        return dropout_qk.matmul(value)

# Initializing the model
model = Model()
 
# Inputs to the model
query  = torch.randn(32, 64, 100, 100)
key   = query.transpose(-1, -2).contiguous()
value = torch.ones_like(query)


