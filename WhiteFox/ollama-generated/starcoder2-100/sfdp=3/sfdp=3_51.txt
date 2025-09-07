
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        v1  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors 
        scale_factor = torch.randn(v1.size()[:-1]) # Get a random scaling factor
        scaled_qk = v1 * scale_factor # Scale the dot product by a random scaling factor 
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.35) # Apply dropout to the scaled dot product 
        v2  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model 
query1, key1, value1 = torch.randn(4096, 8), torch.randn(4096, 513, 513), torch.randn(4096, 257)
__output_model1__  = m(query1, key1, value1)
 
