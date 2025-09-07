
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key):
        qk = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk = qk / 0.7978845608028653
        softmax_qk = F.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=0.1) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, key) # Compute the dot product of the dropout output and the value
        return output
 
