
class Model(torch.nn.Module):
    def __init__(self, scale_factor=0.7071067811865476):
        super().__init__()
        self.scale = scale_factor

    def forward(self, x1, x2):
        qk  = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.div(self.scale)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.5)

        return dropout_qk.matmul(x2)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 3, 64, 64)
x2  = torch.randn(2, 8, 50, 25)
__output__  = m(x1, x2)


