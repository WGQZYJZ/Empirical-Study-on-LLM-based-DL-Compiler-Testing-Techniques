
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, scale_factor, dropout_p=0.1):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk = qk / scale_factor  # Scale the dot product by the scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
        return output
 
# Initializing the model
m = Attention()


def forward(self, query, key, value, scale_factor):
    qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and the key
    scaled_qk = qk / scale_factor  # Scale the dot product by the scale factor
    softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
    dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
    output = dropout_qk.matmul(value)  # Compute the dot product of the dropout output and the value
    return output
# Inputs to the model
query = torch.randn(8, 32, 16, 16)
key = torch.randn(8, 1024, 16, 16)
value = torch.randn(8, 1024, 16, 16)
scale_factor = 1.0  # Scale factor for softmax function applied in the dot product of a query and a key
# 