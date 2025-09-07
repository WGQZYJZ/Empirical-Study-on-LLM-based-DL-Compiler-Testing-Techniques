
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x, y):
        q = self.conv(x)
        k = self.conv(y)

        scale_factor = torch.div(torch.mul(q, k), torch.sqrt(torch.add(torch.pow(k, 2), torch.mul(q, q))))

        dropout_qk = torch.nn.functional.dropout(scale_factor, p=dropout_p)
        output = dropout_qk.matmul(value)

        return output


# Initializing the model
m = Model()
x  = torch.randn(1, 3, 64, 64)
y  = torch.randn(1, 8, 64, 64)
