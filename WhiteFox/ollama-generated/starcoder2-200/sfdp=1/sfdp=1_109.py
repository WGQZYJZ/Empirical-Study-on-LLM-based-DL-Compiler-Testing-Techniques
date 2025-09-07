
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors 
        v2  = v1 / inv_scale_factor # Scale the dot product by the inverse scale factor
        v3  = v2.softmax(dim=-1) # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output 
        return v4 @ value  # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m  = Model()
 
# Inputs to the model
query1 = torch.randn(8, 64, 32)
key1   = torch.randn(8, 32, 32)
value1 = torch.randn(8, 32, 792)
inv_scale_factor1 = 50.
 
# Initial outputs from the model (randomized)
__output__1 = m(query1, key1, value1).shape

# Inputs to the model
query2   = torch.randn(8, 32, 64)
key2     = torch.randn(8, 32, 64)
value2   = torch.randn(8, 792, 64)
inv_scale_factor2  = 10.
 
# Initial outputs from the model (randomized)
__output__2 = m(query2, key2, value2).shape

