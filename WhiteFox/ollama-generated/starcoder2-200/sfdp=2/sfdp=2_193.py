
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        v2 = v1 / (v1.shape[-1]**0.5)  # Scale the dot product by 1/sqrt(n), where n is the number of keys.
        v3 = torch.nn.functional.softmax(v2, dim=-1)
        v4 = torch.nn.functional.dropout(v3, p=0.8, training=self.training) # Apply dropout to the softmax output with a rate of 0.8 when in the training mode, and no dropout otherwise.
        v5 = v4.matmul(value)  # Compute the dot product of the dropout output and the value
        return v5

# Initializing the model
m1 = Model()
 
# Inputs to the model