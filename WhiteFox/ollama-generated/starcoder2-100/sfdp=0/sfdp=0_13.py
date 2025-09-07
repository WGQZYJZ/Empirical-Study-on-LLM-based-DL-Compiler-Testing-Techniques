
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, keys: torch.Tensor, value: torch.Tensor, inv_scale=1):
        v  = torch.matmul(query, keys.transpose(-2, -1)) / inv_scale
        v  = v.softmax(dim=-1)
        return v.matmul(value)


# Initializing the model
m  = Model()

 # Inputs to the model
    q0   = torch.randn(4, 5, dtype=torch.float32)
    k    = torch.randn(768, 4*1/7, 4096).softmax(dim=-1) # [768, 1]
    v    = torch.randn(768, 4096)
    __output__   = m(q0, k, v, inv_scale=torch.sqrt(512))

## End-of-Text
