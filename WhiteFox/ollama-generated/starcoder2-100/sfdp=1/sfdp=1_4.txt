
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1))
        v2  = v1 / 50794386.171875017 
        v3  = v2.softmax(dim=-1)  
        v4  = torch.nn.functional.dropout(v3, p=0.0)   
        v5  = value
        __output__  = v4 @ v5   # Compute the dot product of the dropout output and the value tensor 
        return __output__

# Initializing the model