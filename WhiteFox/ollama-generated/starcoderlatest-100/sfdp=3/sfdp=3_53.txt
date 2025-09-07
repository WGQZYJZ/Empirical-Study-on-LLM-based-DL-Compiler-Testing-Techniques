
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale_factor) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(v1) # Compute the dot product of the dropout output and the value tensor
        return output
 

# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(1, 8, 64, 64) # The query tensor to be transformed
k1 = torch.randn(1, 8, 64, 64) # The key tensor to be used for softmax transformation
v1 = torch.randn(1, 8, 64, 64) # The value tensor that is multiplied by the query tensors using attention
