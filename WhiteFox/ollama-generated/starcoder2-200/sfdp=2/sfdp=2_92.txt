
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor) -> torch.Tensor:
        scale  = math.sqrt(self._key_dim)
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = qk / scale # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=self._dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return output

# Initializing the model
m  = Model()
 
# Inputs to the model
query1  = torch.randn(32, 8096).cuda()
key1  = torch.randn(32, 8096).cuda()
value1  = torch.randn(32, 8096).cuda()
 
m._dropout_p  = 0.5
m._key_dim  = 1 / math.sqrt(3) * math.sqrt(4 + 2 + 3 + 5 + 7) # the output size of the query and key matrix
__output__  = m(query1, key1, value1).shape
 
