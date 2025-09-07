
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, query1, key1, value1):
        v0  = torch.matmul(query1, key1.transpose(-2,-1)) # Compute the dot product of the query and key tensors 
        v3  = scale_factor
        v4  = v0 * v3
        v5  = v4.softmax(dim=-1) 
        v6  = dropout_p
        v7  = torch.nn.functional.dropout(v5, p=v6)
        v8  = v7.matmul(value1) # Compute the dot product of the dropout output and the value tensor
        return v8


# Initializing the model
m0 = Model()


