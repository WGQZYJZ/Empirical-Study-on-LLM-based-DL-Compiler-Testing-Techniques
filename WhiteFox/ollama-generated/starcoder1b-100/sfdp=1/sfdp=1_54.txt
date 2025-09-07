
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        # Use a transpose convolution to compute the dot product of x and key tensors: qk = x @ k.T; scaled_qk = qk / sqrt(scale_factor) 
        # softmax_qk = scaled_qk.softmax(dim=-1); dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p); output = dropout_qk @ value
        # Use a pointwise convolution with kernel size 1 to compute the dot product of x and key tensors: qk = x; scaled_qk = qk / sqrt(scale_factor) 
        # softmax_qk = scaled_qk.softmax(dim=-1); output = torch.nn.functional.conv2d(x, k, stride=1, padding=1).mul(softmax_qk)
        qk = x1 @ x1.transpose(-2, -1) / math.sqrt(math.pi)  # Use a transpose convolution to compute the dot product of x and key tensors: qk = x @ k.T; scaled_qk = qk / sqrt(scale_factor); 
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        value  = dropout_qk @ self.conv(x1)  # Compute the dot product of the dropout output and the value tensor 
        return value

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = x1 * 0.5
x3 = x1 * 0.7071067811865476
x4 = torch.erf(x3)
x5 = x4 + 1
x6 = x2 * x5
