
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_qk = torch.nn.Linear(query.shape[-1], key.shape[-1])
        self.attn_v  = torch.nn.Linear(value.shape[-1], value.shape[-1])
 
    def forward(self, query, key, value):
        qk = self.attn_qk(query).unsqueeze(-2) # Broadcasting on the first dimension of the query tensor
        v  = self.attn_v(value).unsqueeze(-3) # Broadcasting on the last three dimensions of the value tensor

        return ...


# Inputs to the model
query   = torch.randn(batch, dim_q, length_q)
key     = torch.randn(batch, dim_k, length_k)
value   = torch.randn(batch, dim_v, length_v)
