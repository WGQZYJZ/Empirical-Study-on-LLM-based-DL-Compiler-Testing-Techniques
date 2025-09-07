
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = torch.zeros(1, 8)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, x2.transpose(-2, -1))
        scaled_qk = qk / math.sqrt(self.scale_factor + 1e-5)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
