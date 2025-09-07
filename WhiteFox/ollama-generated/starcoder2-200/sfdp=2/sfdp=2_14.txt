
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.matmul(x1[0], x1[2].transpose(-2, -1))  # Compute the dot product of the query and the key
        v2 = v1.div(inv_scale_factor)  # Scale the dot product by the inverse scale factor
        v3 = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v4 = torch.nn.functional.dropout(v3, p=dropout_p)  # Apply dropout to the softmax output
        v5 = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return v6

# Initializing the model
m  = Model()

# Inputs to the model
x1, x2 = [torch.randn(3, 4), torch.randn(4, 4)]
