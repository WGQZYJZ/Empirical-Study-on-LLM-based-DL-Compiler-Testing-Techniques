
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.1, inv_scale_factor=64):
        v1  = torch.matmul(query,key.transpose(-2,-1)) # Compute the dot product of a query and a key
        v2  = v1.div(inv_scale_factor) 
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.5) # Apply dropout to the softmax output
        return v4.matmul(value),v1
 
# Initializing the model
m  = Model()

 # Inputs to the model
    query  = torch.randn(64,28*28).div_(query_scale) # Normalize the query input
    key    = torch.randn(30,57,30) / (key_scale*key_channels) # Normalize the key input
    value  = torch.randn(30,900,416)/value_scale # Normalize the value input
    dropout_p   = 0.8 * 0.1 # Initialize the dropout probability
    inv_scale_factor = 56
# __output__ is a tuple of two tensors: 
    __output__  = m(query,key,value,dropout_p=dropout_p,inv_scale_factor=inv_scale_factor)

