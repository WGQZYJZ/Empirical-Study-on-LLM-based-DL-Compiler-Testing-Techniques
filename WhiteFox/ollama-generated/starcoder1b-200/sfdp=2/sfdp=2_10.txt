
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        qk = torch.matmul(v1, v1.transpose(-2, -1)) / math.sqrt(float(len(query)))
        scaled_qk = qk.div(math.sqrt(float(len(key))))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        v2 = dropout_qk.matmul(v1)
        return v2


# Initializing the model
m = Model()

