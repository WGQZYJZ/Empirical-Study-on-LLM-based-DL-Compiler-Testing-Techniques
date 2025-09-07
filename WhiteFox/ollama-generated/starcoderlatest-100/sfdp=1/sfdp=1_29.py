
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_q = torch.nn.Linear(3, 10)
        self.linear_k = torch.nn.Linear(2, 8)
 
    def forward(self, x1):
        qk = torch.matmul(self.linear_q(x1), self.linear_k(x2).transpose(-2, -1))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 2, 64, 64)
