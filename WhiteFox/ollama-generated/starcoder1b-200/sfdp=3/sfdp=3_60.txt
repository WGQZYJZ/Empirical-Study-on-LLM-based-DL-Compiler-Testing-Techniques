
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) * scale_factor  # Scale the dot product by a factor
        softmax_qk = qk.softmax(dim=-1)  # Apply softmax to the scaled dot product
        dropout_qk = nn.functional.dropout(softmax_qk, p=dropout_p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(value)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
