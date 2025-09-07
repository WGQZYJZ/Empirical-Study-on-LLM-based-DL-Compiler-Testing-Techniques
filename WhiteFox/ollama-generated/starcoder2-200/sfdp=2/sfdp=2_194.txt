
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 / inv_scale_factor # Scale by the inverse scaling factor
        v3  = scaled_qk.softmax(dim=-1) 
        v4  = dropout_qk.matmul(value)
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
q, k, v  = torch.randn(256, 3072), torch.randn(256, 18923, 3072), torch.randn(256, 18923)
__output__   = m(q, k, v)

