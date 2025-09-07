
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, inv_scale_factor=0.5, dropout_p=0.1):
        v1  = torch.matmul(query,key.transpose(-2,-1)) # compute the dot product of the query and the key
        v2  = v1 /inv_scale_factor # scale the dot product by the inverse scale factor 
        v3  = v2.softmax(dim=-1) # apply softmax to the scaled dot product  
        v4  = torch.nn.functional.dropout(v3, p=dropout_p)
        return v4.matmul(value)
 
 # Initializing the model
 m = Model()

 # Inputs to the model
 query = torch.randn(128,600,512) 
 key   = torch.randn(128,600,512)
 value = torch.randn(128, 397,512)
 
 