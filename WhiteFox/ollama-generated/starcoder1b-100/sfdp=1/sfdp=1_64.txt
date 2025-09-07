
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn((3, 64, 64), dtype=torch.float32))
        self.key = torch.nn.Parameter(torch.randn((8, 3, 10, 12), dtype=torch.float32))
        self.scale = torch.nn.Parameter(torch.zeros((1), dtype=torch.float32))
 
    def forward(self, x):
        qk = torch.matmul(x, self.key)
        scaled_qk = qk.div(self.scale)
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        return torch.matmul(dropout_qk, self.query).transpose(-2, -1)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
