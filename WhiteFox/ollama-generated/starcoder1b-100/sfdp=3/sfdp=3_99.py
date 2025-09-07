
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(10, 16), requires_grad=True)  # Input query
        self.key = torch.nn.Parameter(torch.randn(16, 8), requires_grad=True)  # Input key
        self.value = torch.nn.Parameter(torch.randn(8, 4), requires_grad=True)  # Input value
        self.scale_factor = torch.nn.Parameter(torch.ones(10) / math.sqrt(16))  # Factor of scale
        self.dropout_p = 0.5  # Dropout rate
        
    def forward(self, x):
        qk = torch.matmul(x, self.query)  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(self.scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        out = dropout_qk.matmul(x, self.value)  # Compute the dot product of the dropout output and the value tensor
        return out

# Initializing the model
m = Model()

