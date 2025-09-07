
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) 
        v2  = v1 / inv_scale_factor
        v3  = v2.softmax(dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) 
        return v4.matmul(value)

# Initializing the model
m  = Model()
 
# Inputs to the model
query  = torch.randn(2000, 1960).uniform_() - 0.5
key    = torch.randn(1960, 4380).uniform_() - 0.5
value  = torch.randn(1960, 4380)

__output__  = m(query, key, value)

