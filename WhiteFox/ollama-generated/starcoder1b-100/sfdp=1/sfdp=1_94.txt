
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(320, 8)
        self.fc2 = torch.nn.Linear(8, 16)
 
    def forward(self, x1):
        qk = torch.matmul(x1, x1.transpose(-2, -1)) / math.sqrt(math.pi)
        scaled_qk = qk.div(math.sqrt(320))
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = F.dropout(softmax_qk, p=0.2)
        x2 = torch.matmul(dropout_qk, x1)
        return x2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 128, requires_grad=True)
