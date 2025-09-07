
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(768, 1024)
        self.fc2 = torch.nn.Linear(1024, 128)
        self.fc3 = torch.nn.Linear(128, 10)

    def forward(self, x):
        # Forward pass
        q = torch.randn(16, 768)
        k = torch.randn(16, 1024)
        v = torch.randn(16, 128)

        # Compute the dot product of the query and key tensors
        qk = torch.matmul(q, k.transpose(-2, -1))
        # Scale the dot product by a factor
        qk = qk * scale_factor
        # Apply softmax to the scaled dot product
        softmax_qk = qk.softmax(dim=-1)
        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        # Compute the dot product of the dropout output and the value tensor
        output = dropout_qk.matmul(value)

        return output


# Initializing the model
m = Model()


