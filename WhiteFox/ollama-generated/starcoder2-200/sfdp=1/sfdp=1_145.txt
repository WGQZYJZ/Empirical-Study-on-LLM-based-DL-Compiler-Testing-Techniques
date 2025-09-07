
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.5):  # Default values for the dropout probability and the scale factor of dot product
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / math.sqrt(key.size(-1))        # Scale the dot product by an inverse square root scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)           # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
 
        v  = dropout_qk.matmul(value)                   # Compute the dot product of the dropout output and the value tensor
        return v

# Initializing the model
m  = Model()

# Inputs for the model
q1, k2, v3  = [torch.randn((500, 4096)) for _ in range(3)] # Shape (500, 4096) is used to match the scale factor in the previous model
__output__  = m(q1, k2, v3, dropout_p=0.7)

