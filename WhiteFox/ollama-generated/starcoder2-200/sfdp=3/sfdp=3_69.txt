
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors 
        v2  = v1 * scale_factor                            # Scale the dot product by a factor 
        v3  = softmax(v2)                                  # Apply softmax to the scaled dot product 
        v4  = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output 
        v5  = v4 * value                                   # Compute the dot product of the dropout output and the value tensor 
        return v5

# Initializing the model
query = torch.randn(batch_size, heads*head_dim)
key   = torch.randn(batch_size, 3*heads*head_dim) 
value = torch.randn(batch_size, 3*heads*head_dim)
 
m = Model()

