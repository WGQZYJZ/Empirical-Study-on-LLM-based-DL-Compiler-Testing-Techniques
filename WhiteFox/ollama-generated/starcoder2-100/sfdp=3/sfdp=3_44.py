
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
        self.linear2 = torch.nn.Linear(5, 6)
 
    def forward(self, x):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(scale_factor) 
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p) 
        output  = dropout_qk.matmul(value)
        return self.linear1(x), self.linear2(output)


# Initializing the model
m = Model()

# Inputs to the model
query  = torch.randn(5,3)
key   = torch.randn(5,6)
scale_factor  = 0.7894
dropout_p     = 1/2
value          = torch.randn(5,8)
x              = torch.randn(5,3)

