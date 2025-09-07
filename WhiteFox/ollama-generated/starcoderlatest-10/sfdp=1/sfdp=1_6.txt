
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(32, 64)
        self.key = torch.nn.Linear(64, 64)
        self.value = torch.nn.Linear(64, 128)
 
    def forward(self, x1):
        qk = self.query(x1).matmul(self.key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(self.value)
        return output
