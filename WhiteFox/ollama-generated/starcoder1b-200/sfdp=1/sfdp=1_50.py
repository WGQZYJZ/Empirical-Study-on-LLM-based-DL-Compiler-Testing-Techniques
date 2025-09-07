
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1, x2, k_t):
        qk  = torch.matmul(x1, x2.transpose(-2, -1))  # Compute the dot product of two tensors x1 and x2
        scaled_qk  = qk.div(torch.sqrt(float(math.pow(d_kv, -0.5)) + 1e-7)) # Scale the dot product by an inverse scale factor
        softmax_qk  = scaled_qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        output = dropout_qk.matmul(k_t)  # Compute the dot product of the dropout output and the value tensor
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
k_t  = torch.randn(1, 2, 64, 64)
