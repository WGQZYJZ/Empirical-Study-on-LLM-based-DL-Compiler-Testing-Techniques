
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(16, 128) 
        self.key = torch.nn.Linear(16, 128) 

    def forward(self, x1):
        qk = torch.matmul(self.query(x1), self.key(x1).transpose(-2, -1))
        scaled_qk = qk / math.sqrt(128)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(self.value)
        return output
 

# Inputs to the model
x1 = torch.randn(2048, 16, 16)
