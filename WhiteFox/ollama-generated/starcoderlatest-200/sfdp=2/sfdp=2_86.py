
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(1024, 8)
        self.key = torch.nn.Linear(1024, 8)
        self.value = torch.nn.Linear(1024, 8)
 
    def forward(self, x):
        qk = torch.matmul(self.query(x), self.key(x).transpose(-2, -1))
        scaled_qk = qk / np.sqrt(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(self.value(x))
        return output


# Inputs to the model
x = torch.randn(4, 1024, 64, 64)
