
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) * 0.5 # Multiply the query by itself twice
        softmax_qk = qk / 3  # Scale the dot product by half
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk * x1 # Multiply the dropout output and the query element-wise
        return output
# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
