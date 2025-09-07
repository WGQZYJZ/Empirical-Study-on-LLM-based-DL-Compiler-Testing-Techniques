
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 4)
        self.key = torch.nn.Linear(8, 16)
        self.value = torch.nn.Linear(32, 256)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key(x).transpose(-2, -1)) # Compute the dot product of the query and key tensors
        scaled_qk = qk / math.sqrt(32) # Scale the dot product by 0.5
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1) # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
        output = torch.matmul(dropout_qk, self.value(x)) # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(20, 3, 64, 64)
