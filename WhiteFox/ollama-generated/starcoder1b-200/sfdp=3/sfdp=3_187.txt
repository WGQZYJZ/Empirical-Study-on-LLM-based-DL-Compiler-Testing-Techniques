
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn(1, 4, 32))
        self.key = torch.nn.Parameter(torch.randn(1, 4, 32))
        self.scale_factor = 1

    def forward(self, query, key, value):
        qk = torch.matmul(query, key)
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(value)
# Initializing the model
m = Model()


