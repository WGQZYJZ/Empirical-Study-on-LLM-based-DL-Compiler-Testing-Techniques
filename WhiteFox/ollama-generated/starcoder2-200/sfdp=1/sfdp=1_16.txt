
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, dropout_p=0.1, inv_scale_factor = 64): 
        v2 = torch.matmul(query, key.transpose(-2,-1)) / inv_scale_factor
        v3 = v2.softmax(dim=-1) # Softmax
        v7 = torch.nn.functional.dropout(v3, p=dropout_p) # Dropout
        v4  = v7.matmul(value)
        return v4

# Initializing the model
m = Model()

 # Inputs to the model 
 query  = torch.randn(2048,1024)
 key    = torch.randn(2048,1024)
 value  = torch.randn(2048,1025)
 
__output__   = m(query,key,value)
 
