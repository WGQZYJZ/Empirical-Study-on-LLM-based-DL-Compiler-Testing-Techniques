
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk, key, value):
        scaled_qk = torch.nn.functional.linear(qk, scale_factor) # Scale the dot product by a scale factor
        softmax_qk = torch.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = dropout_qk @ value.transpose(-2, -1) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
qk = torch.randn(1, 8, 64, 64) # qk.shape == (1, 8, 64, 64)
key = torch.randn(2, 8, 64, 64) # key.shape == (2, 8, 64, 64)
value = torch.randn(3, 8, 64, 64) # value.shape == (3, 8, 64, 64)
