
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8)
        self.key   = torch.nn.Linear(3, 4)

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scale_factor = torch.rsqrt(torch.pow(qk, 0.5) + epsilon)  # Scale the dot product by a factor
        softmax_qk = qk / scale_factor  # Apply softmax to the scaled dot product
        dropout_qk = F.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return torch.matmul(dropout_qk, x2)  # Compute the dot product of the dropout output and the value tensor

# Initializing the model
m = Model()


