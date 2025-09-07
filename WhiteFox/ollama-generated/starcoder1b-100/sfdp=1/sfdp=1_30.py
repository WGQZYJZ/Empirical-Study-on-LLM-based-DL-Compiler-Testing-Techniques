
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        scaled_v1 = v1.div(0.5).div_(0.7071067811865476)
        softmax_v1  = scaled_v1.softmax(-1)
        dropout_v1 = torch.nn.functional.dropout(softmax_v1, p=dropout_p)
        v2 = v1 * dropout_v1
        output = v2.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
