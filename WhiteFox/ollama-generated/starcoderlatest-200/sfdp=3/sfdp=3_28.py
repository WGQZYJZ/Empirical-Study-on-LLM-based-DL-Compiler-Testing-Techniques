
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, scale_factor):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5) # Apply dropout to the softmax output
        output = dropout_qk.matmul(key) # Compute the dot product of the dropout output and the key tensor
        return output
 
 # Initializing the model
m = Model()
 
# Inputs to the model
query  = torch.randn(1, 32, 56, 56)
key    = torch.randn(1, 32, 56, 56)
scale_factor = torch.randn(())
