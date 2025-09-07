
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()
        self.query = torch.nn.Linear(3, 8)
 
    def forward(self, x1, key):
        v1 = self.dropout(x1)
        qk = torch.matmul(v1, self.query(key).transpose(-2, -1))
        scaled_qk = qk / math.sqrt(key.shape[-1])
        softmax_qk = torch.nn.functional.softmax(scaled_qk, dim=-1)
        dropout_qk = self.dropout(softmax_qk)
        output = dropout_qk.matmul(self.query(v1).transpose(-2, -1))
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key = torch.randn(1, 8, 64, 64)
