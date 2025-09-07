
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_q = torch.nn.Linear(3, 4)
        self.fc_k = torch.nn.Linear(3, 8)
 
    def forward(self, q1, k1, v1):
        scaled_qk = torch.matmul(self.fc_q(q1), self.fc_k(k1).transpose(-2, -1)).div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(self.fc_v(v1))
        return output

 # Inputs to the model
q1 = torch.randn(1, 3, 64, 64)
k1 = torch.randn(1, 3, 64, 64)
v1 = torch.randn(1, 8, 64, 64)
