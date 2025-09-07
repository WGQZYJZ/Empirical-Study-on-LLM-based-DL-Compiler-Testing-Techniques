
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q, k, v, scale=None, dropout_p=0):
        inv_scale  = 1. if (scale is None) else torch.rsqrt(scale).to(q.dtype)
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) * inv_scale 
        v2        = torch.nn.functional.dropout(scaled_qk.softmax(dim=-1), p=dropout_p)
        v3        = v2.matmul(v)
        return v3

# Initializing the model 
m = Model()

 # Inputs to the model 
 q   = torch.randn([5, 4, 3])
 k   = torch.randn([5, 3, 7])
 v1  = torch.randn([5, 4, 7])
 
 __output__  = m(q, k, v1)

