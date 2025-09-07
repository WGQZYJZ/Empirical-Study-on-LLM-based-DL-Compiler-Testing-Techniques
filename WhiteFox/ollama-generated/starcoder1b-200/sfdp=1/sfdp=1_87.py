
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q = torch.nn.Linear(32, 8)
        self.k = torch.nn.Linear(64, 16)
        self.v = torch.nn.Linear(64, 32)

    def forward(self, x):
        k = self.k(x).transpose(-2, -1)  # Compute the dot product of the key and input tensors
        q = self.q(x).transpose(-2, -1)
        scaled_qk = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(math.pow(self.dim, -0.5))  # Scale the dot product by the inverse scale factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v = self.v(x).transpose(-2, -1)  # Compute the dot product of the value and input tensors
        output = dropout_qk.matmul(v)  # Compute the dot product of the dropout output and the value tensor
        return output


# Initializing the model
m = Model()


