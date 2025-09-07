
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.key = torch.nn.Embedding(10, 8)
 
    def forward(self, x1, x2, query, key, value, inv_scale_factor, dropout_p=None):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk.div(inv_scale_factor) # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()
query = torch.randn(2048, 64).transpose(-2, -1)
key = m.key(x2)
inv_scale_factor = key.shape[1] ** -0.5
value = torch.randn(2048, 1, 64, 64)
# Inputs to the model
query = query / inv_scale_factor # Scale by the inverse scale factor
query = query.transpose(-2, -1) # Transpose batch and sequence dimensions so that they appear last
x1 = torch.randn(1, 8, 32, 32).div(255) # Normalize image data to range [0-1] and convert the image format to (batch size, channel, width, height), where "channel" is either one or three.


# Output of the model on generated input tensor x1
