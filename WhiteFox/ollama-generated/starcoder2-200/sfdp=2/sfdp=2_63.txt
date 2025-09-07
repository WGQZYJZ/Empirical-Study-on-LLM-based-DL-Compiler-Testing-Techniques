
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dot  = torch.nn.Linear(8, 1)
 
    def forward(self, query: torch.Tensor, key: torch.Tensor, value: torch.Tensor, dropout_p=0.5, scale_factor=2):
        qk  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        scaled_qk  = qk / float(scale_factor) # Scale the dot product by an inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output  = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value
        return self.dot(output), qk

# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(3, 160, 8)
key   = torch.randn(3, 257, 8)
value = torch.randn(3, 240, 8)

__output__, _ = m(query, key, value)

