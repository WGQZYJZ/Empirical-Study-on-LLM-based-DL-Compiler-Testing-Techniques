
class Model(torch.nn.Module):
    def __init__(self, scale_factor=0.5, p=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.softmax = torch.nn.functional.softmax

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * scale_factor
        qk = torch.matmul(v2, x2.transpose(-2, -1))  # Compute the dot product of v2 and x2
        softmax_qk = self.softmax(qk)  # Apply softmax to the scaled dot product
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=p)  # Apply dropout to the softmax output
        return dropout_qk.matmul(x2)  # Compute the dot product of the dropout output and x2


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
