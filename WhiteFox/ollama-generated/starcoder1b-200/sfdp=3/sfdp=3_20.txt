
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        # Apply pointwise convolution with kernel size 1 to the input tensor
        qk = torch.matmul(x1, x1.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        scaled_qk = qk.mul(scale)  # Scale the dot product by a factor

        # Apply softmax to the scaled dot product
        softmax_qk = scaled_qk.softmax(dim=-1)

        # Apply dropout to the softmax output
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        # Compute the dot product of the dropout output and the value tensor
        return torch.matmul(dropout_qk, x2)


# Initializing the model
m = Model()

