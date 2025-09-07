
class Model(torch.nn.Module):
    def __init__(self, dropout_p=0.15):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of x1 and x1
        scale_factor = torch.rsqrt(qk + 1e-9)  # Use sqrt function to compute the inverse of the reciprocal sqrt of qk
        scaled_qk = qk.div(scale_factor)
        softmax_qk = scaled_qk.softmax(-1)  # Apply softmax to the scaled dot product
        output = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value = torch.matmul(output, key)  # Compute the dot product of the dropout output and the value
        return value


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
