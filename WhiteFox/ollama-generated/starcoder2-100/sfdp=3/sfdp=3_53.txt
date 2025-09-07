
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 8)

    def forward(self, x1):
         qk  = self.linear(x1).matmul(self.linear(x1)) # Compute the dot product of a linear output and another linear output
         scaled_qk  = qk * scale_factor # Scale the result by a factor
         softmax_qk  = scaled_qk.softmax(dim=-1) # Apply softmax to the scaled result
         dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p) # Apply dropout to the softmax output
         output  = dropout_qk.matmul(self.linear(x1)) # Compute a dot product of another linear output and the dropout output
# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(2) # Generate random input tensor with shape (batch, 2), this is where we will feed the query. Also, the output of this linear layer should be used as an input to another linear layer.

