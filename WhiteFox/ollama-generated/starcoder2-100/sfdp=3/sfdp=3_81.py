
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1)) * scale_factor 
        v2  = torch.softmax(v1, dim=-1) # softmax
        v3  = nn.functional.dropout(v2, p=dropout_p) 
        v4  = v3.matmul(value)
        return v4
# Initializing the model
m = Model()


# Inputs to the model
x0  = torch.randn(16,  5,   8)
x1  = torch.randn(16,  7,   9) # different from previous one
__output__  = m(x0, x1, x0 + x1)

