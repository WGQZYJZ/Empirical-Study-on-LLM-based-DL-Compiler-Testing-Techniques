
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(256, 10)
        self.key   = torch.nn.Linear(256, 10)
 
    def forward(self, q1, k1):
        qk = torch.matmul(q1, k1.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output

# Inputs to the model
q1  = torch.randn(1, 1024, 768)
k1  = torch.randn(1, 1024, 768)
