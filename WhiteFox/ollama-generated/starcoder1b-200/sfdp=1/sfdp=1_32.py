
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(7, 5)
        self.key   = torch.nn.Linear(1, 4)
        self.value = torch.nn.Linear(3, 4)
 
    def forward(self, x):
        qk = torch.matmul(x.transpose(-2, -1), self.query(x))
        scaled_qk = qk.div(torch.sqrt(torch.ones_like(qk)))
        softmax_qk = F.softmax(scaled_qk, dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=0.2)
        output = dropout_qk.matmul(self.value(x))
        return output


# Inputs to the model
x  = torch.randn(8, 7)
