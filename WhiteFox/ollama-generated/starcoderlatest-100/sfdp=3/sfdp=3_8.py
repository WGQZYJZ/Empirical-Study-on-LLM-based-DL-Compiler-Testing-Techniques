
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear_q = torch.nn.Linear(3, 8)
        self.linear_k = torch.nn.Linear(64, 8)
        self.linear_v = torch.nn.Linear(64, 8)
 
    def forward(self, x1):
 
        query = self.linear_q(x1)
        key   = self.linear_k(x2)
        value = self.linear_v(x3)
 
        qk = torch.matmul(query, key.transpose(-2, -1)) * scale_factor
        softmax_qk = qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output  = dropout_qk.matmul(value)
 
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 64, 64, 64)
x3 = torch.randn(1, 8, 64, 64)
