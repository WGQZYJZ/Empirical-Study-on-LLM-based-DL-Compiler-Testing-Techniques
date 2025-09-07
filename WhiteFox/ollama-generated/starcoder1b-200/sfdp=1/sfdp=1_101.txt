
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1).view(-1, 8, -1)  # Shape of v1: [-1, 8, 64, 64]
        qk = torch.matmul(v1, v1.transpose(-2, -1))  # Shape of qk: [-1, 8, 8, 8]
        scaled_qk = qk.div(torch.norm(qk, p=2, dim=-1).view(
            -1, 1).expand(-1, 8))  # Shape of v1: [-1, 8, 64, 64]
        softmax_qk = scaled_qk.softmax(dim=-1)  # Shape of v1: [-1, 8, 64, 64]
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)  # Shape of v1: [-1, 8, 64, 64]
        return dropout_qk.matmul(value).view(-1, 32)  # Shape of output: [-1, 32]


# Initializing the model
m = Model()


