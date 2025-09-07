
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        v2  = torch.matmul(q1, k1.transpose(-2, -1)) 
        v3  = v2 / inv_scale_factor
        v4  = v3.softmax(dim=-1) 
        v5  = torch.nn.functional.dropout(v4, p=dropout_p) 
        return v5 @ v1


# Initializing the model
m  = Model()
 
# Inputs to the model
q1  = torch.randn(20,37,64)
k1  = torch.randn(20,64,64)
v1  = torch.randn(20,64,384)
__output__  = m(q1, k1, v1)

