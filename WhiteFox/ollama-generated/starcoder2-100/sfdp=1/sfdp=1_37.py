

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        v2  = v1 / (10 ** -4)                           # Scale the dot product by an inverse scale factor
        v3  = v2.softmax(dim=-1)                        # Apply softmax to the scaled dot product
        v4  = torch.nn.functional.dropout(v3, p=0.5)    # Apply dropout to the softmax output
        return v4.matmul(value)                         # Compute the dot product of the dropout output and the value tensor
 

# Initializing the model
m  = Model()


# Inputs to the model