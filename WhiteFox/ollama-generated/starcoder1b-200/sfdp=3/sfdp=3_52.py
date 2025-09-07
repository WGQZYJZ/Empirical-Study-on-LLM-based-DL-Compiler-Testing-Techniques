
class Model(torch.nn.Module):
    def __init__(self, scale_factor=1.0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.scale_factor = scale_factor
 
    def forward(self, x1, key, value, dropout_p=None):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, key.transpose(-2, -1))
        s_qk = qk.mul(self.scale_factor)
        softmax_qk = s_qk.softmax(dim=-1)
        if dropout_p is not None:
            output = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        else:
            output = softmax_qk.matmul(value)
        return output


# Initializing the model
m = Model()


