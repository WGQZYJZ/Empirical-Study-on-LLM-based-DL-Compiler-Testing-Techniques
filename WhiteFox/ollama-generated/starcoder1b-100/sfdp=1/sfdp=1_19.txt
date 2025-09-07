
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        qk = torch.matmul(x1, x2).div(torch.pow(query_scale_factor, -2)).softmax(-1)
        return torch.nn.functional.dropout(qk.matmul(x3), p=dropout_p)


# Initializing the model
m = Model()


