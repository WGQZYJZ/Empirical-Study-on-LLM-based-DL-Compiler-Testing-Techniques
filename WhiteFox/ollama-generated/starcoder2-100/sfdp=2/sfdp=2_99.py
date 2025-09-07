
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        v2  = torch.matmul(q1, k1)
        v3  = v2 / inv_scale_factor
        v4  = v3.softmax(dim=-1) 
        v5  = v4.dropout(p=dropout_p)
        return v5 @ v1


# Initializing the model
m  = Model()

# Inputs to the model
__query, __key,__value  =  torch.randn(64, 32),torch.randn(64, 32, 32),torch.randn(32)


