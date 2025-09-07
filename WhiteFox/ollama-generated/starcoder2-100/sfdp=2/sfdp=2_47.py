
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, q1, k1, v1):
        v2  = torch.matmul(q1, k1) 
        v3  = v2 / inv_scale_factor # Scaling
        v4  = v3.softmax(-1)        # Apply softmax
        v5  = torch.nn.functional.dropout(v4, p=dropout_p)  # Apply dropout
        v6  = v5 @ v1               # Compute the dot product of the dropout output and a value
        return v6


# Initializing the model