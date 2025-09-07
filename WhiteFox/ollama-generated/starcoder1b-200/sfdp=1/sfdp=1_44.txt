
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(input_size, hidden_size)
 
    def forward(self, x1, x2):
        k  = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(hidden_size)
        qk = k * 0.5
        softmax_qk = torch.nn.functional.softmax(qk, dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4, 8, 64)
x2 = torch.randn(1, 3, 64, 8)
