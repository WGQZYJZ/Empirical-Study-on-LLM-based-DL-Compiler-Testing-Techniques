
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()
        self.linear_k = torch.nn.Linear(128, 128)
 
    def forward(self, x):
        qk = torch.matmul(x, self.linear_k(x))
        scaled_qk = qk / math.sqrt(128) # Scale the dot product by sqrt(d_k)
        softmax_qk = scaled_qk.softmax(-1) # Apply softmax to the scaled dot product
        dropout_qk = self.dropout(softmax_qk) # Apply dropout to the softmax output
        output = dropout_qk.matmul(x) # Compute the dot product of the dropout output and the value tensor
        return output
 
# Inputs to the model
x = torch.randn(1, 64, 256)
