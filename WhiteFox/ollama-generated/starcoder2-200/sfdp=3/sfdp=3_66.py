
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout  = torch.nn.Dropout2d()
        self.softmax = torch.nn.Softmax(-1)
 
    def forward(self, query, key, value, dropout_p=0.5):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of two tensors in one operation
        v2  = self.softmax(v1 / math.sqrt(query.size(-1))) # Apply Softmax to the output of the dot product, and then divide by a square root of the last dimension of query
        v3  = torch.nn.functional.dropout(v2, p=0) # Dropout the output of the softmax layer using an elementwise dropout
        __output__  = self.dropout(value) * v3 # Apply dropout to value and then multiply the result by the dot product of two tensors in one operation
        return v1


# Initializing the model
m  = Model()
 
# Inputs to the model
q, k, v  = torch.randn(128, 1024), torch.randn(512, 1024), torch.randn(512, 512) # Create three randomly initialized tensors of size (128, 1024).

