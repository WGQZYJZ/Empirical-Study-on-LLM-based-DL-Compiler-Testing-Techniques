
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, query1234567890, key, value):
        inv_scale  = torch.full((query1234567890.size(-1)), -1/5)  # Initialize a vector to -0.2
        dropout_p = 0.00  # Set the dropout probability to zero
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk  = qk / inv_scale  # Scale the dot product by an inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m  = Model()

# Inputs for the model, note that the shape must be valid. Please make sure to set a proper shape.
query1234567890  = torch.randn(size=(1, 5)) # Replace with the query input tensor of the previous example.
key  = torch.randn(size=(1, 5)) # Replace with the key input tensor of the previous example.
value  = torch.randn(size=(1, 240798035)) # Replace with a value input tensor.

