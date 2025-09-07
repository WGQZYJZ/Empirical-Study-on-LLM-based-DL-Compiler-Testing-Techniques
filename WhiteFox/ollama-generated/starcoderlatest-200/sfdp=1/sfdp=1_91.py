
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv_conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2, x3):
        qk = torch.matmul(x1, x2)
        qk = torch.matmul(qk, x3.transpose(-2, -1))
        scaled_qk = qk / (scale_factor**0.5)
        softmax_qk = torch.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, dropout_p)
        output = dropout_qk.matmul(x4)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(8, 3, 16, 16)
x3 = torch.randn(8, 3, 16, 16)
