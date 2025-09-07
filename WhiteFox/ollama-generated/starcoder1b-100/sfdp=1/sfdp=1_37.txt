
class Model(torch.nn.Module):
    def __init__(self, hidden_dim):
        super().__init__()
        self.query = torch.nn.Linear(hidden_dim, hidden_dim)
        self.key   = torch.nn.Linear(hidden_dim, hidden_dim)
        self.value = torch.nn.Linear(hidden_dim, hidden_dim)
 
    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk  = qk.div(math.sqrt(self.key_dim))  # Scale the dot product by the inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        y  = dropout_qk.matmul(x2)        # Compute the dot product of the dropout output and the value tensor
        return y
 

# Initializing the model
m = Model(hidden_dim)


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 8, 64, 64)
