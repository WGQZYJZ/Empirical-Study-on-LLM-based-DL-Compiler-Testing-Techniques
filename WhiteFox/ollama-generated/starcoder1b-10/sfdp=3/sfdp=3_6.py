
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, scale_factor=1.0):
        k1 = self.conv(x1).mul(scale_factor)
        k2 = torch.mm(x1, x2.transpose(-2, -1))  # Compute the dot product of the query and key tensors
        qk = torch.matmul(k1, k2)
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, x2)
        return output


# Initializing the model
m = Model()


