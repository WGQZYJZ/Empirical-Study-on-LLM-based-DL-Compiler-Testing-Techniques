
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k2, v3):
        v4  = torch.matmul(q1, k2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        v5  = v4 / inv_scale_factor # Scale the dot product by the inverse scale factor
        v6  = v5.softmax(dim=-1) # Apply softmax to the scaled dot product
        v7  = torch.nn.functional.dropout(v6, p=dropout_p) # Apply dropout to the softmax output
        v8  = v7.matmul(v3) # Compute the dot product of the dropout output and the value tensor
        return v8


# Initializing the model