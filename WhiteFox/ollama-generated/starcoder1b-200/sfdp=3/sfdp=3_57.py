
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(128, 64)  # Define a linear layer
        self.key   = torch.nn.Linear(128, 64)
        self.value = torch.nn.Linear(128, 3)
        self.scale_factor = nn.Parameter(torch.ones((32,)))

    def forward(self, x):
        query = self.query(x)
        key   = self.key(x)
        value = self.value(x)

        qk = torch.matmul(query, key.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(self.scale_factor)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = nn.functional.dropout(softmax_qk, p=self.p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(value)


# Inputs to the model
x = torch.randn(1, 128)
