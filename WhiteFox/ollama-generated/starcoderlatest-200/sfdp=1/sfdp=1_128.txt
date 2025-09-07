
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / math.sqrt(query.shape[-1])  # Scale the dot product by the square root of the output dimension
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.7)  # Apply dropout to the softmax output
        output = dropout_qk @ value  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
a = Attention()


# Inputs to the model
query = torch.randn(32, 8, 64, 64)
key   = torch.randn(32, 8, 64, 64)
value = torch.randn(32, 8, 64, 64)
