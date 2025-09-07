
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(5, 2)
        self.key    = torch.nn.Linear(3, 4)
        self.value  = torch.nn.Linear(4, 6)
        self.scale  = torch.nn.Parameter(torch.ones(1))
 
    def forward(self, x1):
        qk   = self.query(x1).matmul(self.key.transpose(-2, -1))  # Compute the dot product of the query and the key
        scaled_qk  = qk.div(self.scale)  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v   = dropout_qk.matmul(self.value(x1))  # Compute the dot product of the dropout output and the value
        return v

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5, 64, 64)
