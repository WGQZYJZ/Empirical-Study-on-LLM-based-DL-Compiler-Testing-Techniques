
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 32)
        self.key   = torch.nn.Linear(32, 32)
        self.value = torch.nn.Linear(32, 64)
 
    def forward(self, query, key, value):
        qk   = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk    = qk.mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v         = dropout_qk.matmul(value)   # Compute the dot product of the dropout output and the value tensor
        return v


# Initializing the model
m = Model()


