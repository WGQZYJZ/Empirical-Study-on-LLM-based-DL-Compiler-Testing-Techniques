
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query  = torch.nn.Linear(8, 16)
        self.key    = torch.nn.Linear(8, 32)
        self.value  = torch.nn.Linear(32, 1)
 
    def forward(self, x):
        q   = self.query(x)  # Compute the output of the query tensor
        k   = self.key   (x)  # Compute the output of the key tensor
        v   = self.value (x)  # Compute the output of the value tensor
        scaled_qk  = torch.matmul(q, k).mul(scale_factor)  # Scale the dot product by a factor
        softmax_qk  = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor


# Initializing the model
m = Model()


