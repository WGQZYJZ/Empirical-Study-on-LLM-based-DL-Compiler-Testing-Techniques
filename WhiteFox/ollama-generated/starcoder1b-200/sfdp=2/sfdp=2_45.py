
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(d_model, d_k)  # Linear layer that computes `qk` and softmax output from the query and key
        self.value = torch.nn.Linear(d_v, d_v)  # Linear layer that computes `value` from the dropout output of the previous step
        self.key = torch.nn.Linear(d_k, d_k)  # Linear layer that computes `key` and softmax output from the query and key

    def forward(self, x1, x2):
        kq  = self.query(x1).matmul(self.key(x2).transpose(-2, -1))
        v = self.value(dropout_p * (self.value(x1) + self.value(x2)))
        k = self.key(x1)
        scaled_qk  = kq.div(math.sqrt(k.size(-1).float().to(dtype=x1.device)))
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
