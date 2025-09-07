
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_norm = torch.nn.LayerNorm([4, 8])
 
    def forward(self, qk):
        v1 = torch.matmul(qk, k) # Compute the dot product of the query and key tensors
        v2 = v1 * scale_factor
        v3 = softmax(v2, dim=-1) # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=dropout_p) # Apply dropout to the softmax output
        v5 = torch.matmul(v4, v) # Compute the dot product of the dropout output and the value tensor
        return v5


# Initializing the model
m = Model()

# Query and key tensors to the attention mechanism with different dimensions
qk  = torch.randn(1, 8, 20496, 4)
v   = torch.randn(1, 8, 4096, 256)
