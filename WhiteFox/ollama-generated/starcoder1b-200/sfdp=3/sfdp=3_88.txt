
class Model(torch.nn.Module):
    def __init__(self, d_k, d_v, nhead):
        super().__init__()
        self.d_k = d_k
        self.d_v = d_v
        self.nhead = nhead

        self.qk = torch.nn.Linear(d_k, nhead * d_k)
        self.wk = torch.nn.Linear(d_v, nhead * d_k)
        self.wv = torch.nn.Linear(d_v, nhead * d_k)

        self.softmax = torch.nn.Softmax(dim=-1)

    def forward(self, x1, x2):
        qk = self.qk(x1).matmul(self.wk(x2))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(self.d_k ** -0.5)  # Scale the dot product by a factor
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)  # Apply dropout to the softmax output
        value = dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and the value tensor
        return self.value

    def __repr__(self):
        return f'<Model d_k={self.d_k}, d_v={self.d_v}, nhead={self.nhead}>'

# Initializing the model
m = Model(20, 10, 4)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
