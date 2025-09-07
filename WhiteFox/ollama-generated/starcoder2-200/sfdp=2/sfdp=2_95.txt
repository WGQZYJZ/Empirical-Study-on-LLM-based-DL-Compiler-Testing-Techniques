
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul  = torch.nn.Linear(128, 37)
        self.dropout  = torch.nn.Dropout(0.5)
 
    def forward(self, query_tensor, key_tensor, value_tensor):
        k1  = self.matmul(key_tensor) # Compute the dot product of a query and a key for each dimension by performing a dot product between a query and keys in the last two dimensions and a key and values in the last three dimensions.
        v1  = torch.nn.functional.softmax(k1, dim=-2) 
        v2  = self.dropout(v1) # Apply dropout to the output of the softmax operation.
        return k1.matmul(value_tensor)
 
# Initializing the model
m  = Model()


# Inputs to the model
q  = torch.randn(64, 37)
k  = torch.randn(8092, 128) # In this case, the first dimension (which is the batch size) must be 8092 for proper evaluation, but 32 for visualization reasons.
v  = torch.randn(56447, 128)
 
__output_without_dropout__  = m(q, k, v) # Without dropout: this will throw an error because the first dimension of the query must be 8092 (the size of batch).

__output___ = m.eval() # Switch to evaluation mode and then re-run the forward pass with the same input tensors (to avoid changing the initial seed that was set in the beginning).
__output_with_dropout__  = m(q, k, v) # With dropout: this will throw an error because the first dimension of the query must be greater than or equal to 8092.