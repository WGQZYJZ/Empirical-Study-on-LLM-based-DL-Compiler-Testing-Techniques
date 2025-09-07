
class Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of two input tensors
        v2  = v1 / math.sqrt(3)  # Scale the dot product by a constant sqrt(3)
        v3  = F.softmax(v2, dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=0.5, inplace=True) # Apply dropout to the softmax output
        v5  = v4.matmul(value) # Compute the dot product of the dropout output and a value tensor
        return v5


# Initializing the model with the specified hyperparameters
m = Model(32)
 
# Inputs to the model
query = torch.randn(1, n_query, 64)
key = torch.randn(n_key, 64)
value = torch.randn(n_value, 64)

# Executing the model with the inputs and the hyperparameters specified in the previous cell