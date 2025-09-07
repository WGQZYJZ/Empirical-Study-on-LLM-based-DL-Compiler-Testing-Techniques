
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.15, inv_scale_factor=4):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, query, key, value):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = qk / inv_scale_factor # Scale the dot product by the inverse scale factor 
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product 
        dropout_qk  = self.dropout(softmax_qk) # Apply dropout to the softmax output
        output  = torch.matmul(dropout_qk, value) # Compute the dot product of the dropout output and the value 
        return output


# Initializing the model
m1 = Model()

# Inputs for the first model
q1  = torch.randn(256, 3072)
k1  = torch.randn(256, 3072)
v1  = torch.randn(256, 8192)

# Outputs for the first model
__output___1  = m1(q1, k1, v1)

# Initializing a new model with different parameters and inputs
m2  = Model(dropout_p=0.40, inv_scale_factor=896735)

q2  = torch.randn(128, 1024)
k2  = torch.randn(128, 1024)
v2  = torch.randn(128, 8192)

__output___2  = m2(q2, k2, v2)

