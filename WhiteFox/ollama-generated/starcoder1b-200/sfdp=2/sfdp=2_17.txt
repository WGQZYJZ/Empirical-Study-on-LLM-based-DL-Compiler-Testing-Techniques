
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.fc   = torch.nn.Linear(64 * 4 * 4, 50)
 
    def forward(self, x1):
        qk = torch.matmul(x1, self.conv.weight).transpose(-2, -1)
        scaled_qk = qk.div(1 / math.sqrt(float(qk.shape[-1])))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        x2 = dropout_qk.matmul(self.fc.weight).transpose(-2, -1)
        return x2


# Initializing the model
m  = Model()


