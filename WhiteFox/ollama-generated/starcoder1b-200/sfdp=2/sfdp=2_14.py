
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(in_features, out_features=kdim*4, bias=True)
        self.v = torch.nn.Linear(in_features, out_features=vdim*4, bias=True)
 
    def forward(self, x):
        q  = self.qk(x)
        v  = self.v(x)
        qk = torch.matmul(q, k).div(torch.sqrt(self.scale))
        softmax_qk = qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, v).transpose(-2, -1)
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
