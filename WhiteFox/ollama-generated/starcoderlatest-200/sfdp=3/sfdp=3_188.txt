
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(768, 3072)
 
    def forward(self, q, k, v, scale_factor=None, dropout_p=None):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk * scale_factor
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output


# Inputs to the model
q  = torch.randn(1024, 768).unsqueeze(-2) # shape (1024, 768, 1, 1)
k  = torch.randn(1024, 768).unsqueeze(-3)
v  = torch.randn(1024, 768).unsqueeze(-2)
scale_factor  = 5.7e-5 # shape (1,)
dropout_p  = 0.9
