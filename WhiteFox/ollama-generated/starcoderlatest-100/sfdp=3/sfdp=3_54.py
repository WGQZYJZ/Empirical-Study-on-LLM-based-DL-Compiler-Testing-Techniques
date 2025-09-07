
class Model(torch.nn.Module):
    def __init__(self, scale_factor=1.0, query=None, key=None, value=None):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.matmul(x1, x2)  # Compute the dot product of x1 and x2 tensors
        scaled_v1 = v1.mul(scale_factor)  # Scale the dot product by a factor
        softmax_v1 = scaled_v1.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_v1.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model(scale_factor=4.0, query=key, key=query, value=value)
