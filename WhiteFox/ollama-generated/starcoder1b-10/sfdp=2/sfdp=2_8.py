
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query_conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.key_conv    = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        v = qk.div(torch.linalg.norm(qk))
        qk_ = qk.mul_(scale)
        softmax_qk = nn.functional.softmax(qk_, dim=-1)
        dropout_qk = nn.functional.dropout(softmax_qk, p=dropout_p)
        v = torch.matmul(x2, dropout_qk)
        return v

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 5, 32)
