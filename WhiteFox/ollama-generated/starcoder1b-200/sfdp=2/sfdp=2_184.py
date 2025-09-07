
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        k = x2  # Compute the dot product of the query and a constant value, namely `k`.
        s = v1.softmax(-1)  # Apply softmax to the query
        dk = torch.nn.functional.dropout(s, p=dropout_p)  # Apply dropout to the softmax output
        v2 = dk.matmul(v1)  # Compute the dot product of `dk` and `v1`, namely `v2`.
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
