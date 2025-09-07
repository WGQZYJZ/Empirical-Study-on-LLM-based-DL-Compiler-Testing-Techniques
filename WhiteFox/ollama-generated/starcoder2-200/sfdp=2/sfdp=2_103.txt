
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        v3 = v2 / scale_factor  # Scale the dot product by a constant factor called `scale_factor`
        v4 = v3.softmax(dim=-1) # Apply softmax to the scaled dot product
        v5 = torch.nn.functional.dropout(v4, p=dropout_p) # Apply dropout to the softmax output
        return v5.matmul(value) # Compute the dot product of the dropout output and a value

# Initializing the model
m  = Model()

# Inputs to the model
query = torch.randn(10, 128, 768)
key   = query + 3.5
value = key / 2
__output__  = m(query)

