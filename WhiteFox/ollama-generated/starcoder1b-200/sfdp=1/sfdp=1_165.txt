
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2, attn):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, v2.transpose(-2, -1)) / math.sqrt(kernel_size ** 2)
        scaled_qk = qk.div(math.sqrt(self.scale_factor))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return self.attn(output, attn)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 3, 64, 64)
attn = torch.tensor([[[0.70569448],
                    [0.29032439],
                    [0.40399885]],
                   [[-0.70710678],
                    [-0.43424242],
                    [-0.33322584]]])
