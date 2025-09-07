
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2,-1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m1 = Model()


# Inputs to the model: query, key tensors with shapes (1024L,) and (576L, 1024L). The shape of `value` is variable.
query_input = torch.randn(1024) # Generate random 1-dimensional array of length 1024
key_input = torch.randn(576, 1024)# Generate random 2-dimensional array with dimensions (576L,) and (1024L). The size of the array varies depending on the model and the device where it is being run.
x1 = m1(query_input, key_input)
x1_shape = x1.size() # Get the shape of the output from the model

