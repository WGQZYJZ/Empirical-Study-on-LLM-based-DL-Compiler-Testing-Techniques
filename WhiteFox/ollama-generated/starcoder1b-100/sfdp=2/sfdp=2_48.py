
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(math.pow(self.scale_factor, 2) * x1.size()[-2] * x1.size()[-1])
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output


# Inputs to the model
query = torch.randn(4, 5, 8, 16)
key = torch.randn(4, 5, 16, 16)
scale_factor = math.pow(self.model_size / query.size()[-2] / query.size()[-1], -1)  # Scale the dot product by the inverse scale factor
inv_scale_factor = 1 / scale_factor  # Inverse of the scale_factor
value = torch.randn(4, 5, 16, 8)


