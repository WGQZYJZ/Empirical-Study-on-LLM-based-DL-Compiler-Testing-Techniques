
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk / self.scale_factor  # Scale the dot product by the scale factor
        softmax_qk = torch.nn.functional.softmax(scaled_qk)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.p)  # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, value)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Attention()

# Inputs to the model
query  = torch.randn(1, 256, 32, 768)
key    = torch.randn(1, 256, 2049, 768)
value  = torch.randn(1, 256, 2049, 768)
