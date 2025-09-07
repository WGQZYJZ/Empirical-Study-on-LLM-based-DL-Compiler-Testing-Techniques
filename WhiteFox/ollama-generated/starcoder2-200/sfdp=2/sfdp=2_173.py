
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        qk  = torch.matmul(q1, k1.transpose(-2, -1)) # Compute the dot product of a query and a key 
        scaled_qk  = qk / inv_scale_factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output

        v5  = dropout_qk @ v1  # Compute the dot product of a dropout output and a value
        return v5


# Initializing the model
m  = Model()

# Inputs for the model
q1  = torch.randn(2, 3)
k1  = torch.randn(2, 4, 8)
v1  = torch.randn(4, 9)
 
__output__  = m(q1, k1, v1)
