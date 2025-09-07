
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(1024, 1024)
        self.softmax_qk = torch.nn.Softmax(dim=-1)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = self.softmax_qk(scaled_qk)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = torch.matmul(dropout_qk, value)
        return output


# Inputs to the model
query  = torch.randn(1024, 64)
key    = torch.randn(1024, 64)
value  = torch.randn(1024, 64)
