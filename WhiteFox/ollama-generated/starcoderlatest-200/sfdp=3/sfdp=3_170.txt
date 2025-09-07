
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(24, 5) # Input dimensions: (batch_size, seq_len, input_dims). Output dimensions: (batch_size, seq_len, 5)
        self.linear2 = torch.nn.Linear(150, 30)
 
    def forward(self, query, key):
        v1 = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = v1 * scale_factor # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        v2 = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
        return v2


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(1, 3, 64, 64)
key    = torch.randn(8, 3, 64, 64)
