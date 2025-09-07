
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / 0.5 # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.3) # Apply dropout to the softmax output
        output = dropout_qk.matmul(x2) # Compute the dot product of the dropout output and the value
        return output
# Inputs to the model
x1 = torch.randn(1, 8, 64, 64) # Query
x2 = torch.randn(1, 8, 64, 64) # Key
