
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(1024, 512)
        self.softmax = torch.nn.Softmax(dim=-1)
        self.dropout = torch.nn.Dropout(p=0.5)
 
    def forward(self, x):
        qk = self.matmul(x).matmul(x.transpose(-2, -1))
        scaled_qk = qk.mul(1.0/math.sqrt(float(x.size(-1))))
        softmax_qk = self.softmax(scaled_qk)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(x)
        return output

# Inputs to the model
x1 = torch.randn(1, 1024, 512)
