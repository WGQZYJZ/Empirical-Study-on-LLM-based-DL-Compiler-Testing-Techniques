
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(768, 384)
        self.key   = torch.nn.Linear(768, 192)
        self.value = torch.nn.Linear(192, 384)
 
    def forward(self, x1):
        qk = self.query(x1).matmul(self.key.transpose(-2, -1))
        scaled_qk = qk.mul(0.01) # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.2)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(self.value(x1))  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 768) # Query with shape (batch_size=2, num_heads=1, seq_len=513)
x2 = torch.randn(2, 768) # Key with shape (batch_size=2, num_heads=1, seq_len=513)
x3 = torch.randn(2, 192) # Value with shape (batch_size=2, num_heads=1, seq_len=1024)
