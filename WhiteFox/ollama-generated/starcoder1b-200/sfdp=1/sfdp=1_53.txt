
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x, key_q, value, query, key, dropout_p=0.5):
        v = self.conv(x)
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(torch.sqrt(torch.mean(qk**2, dim=1)))  # Scale the dot product by an inverse of its square root
        softmax_qk = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        v = dropout_qk.matmul(value)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
key_q = torch.randn(1, 8, 256)
value = torch.randn(1, 8)
query = torch.randn(1, 8, 256)
key = torch.randn(1, 8, 256)
