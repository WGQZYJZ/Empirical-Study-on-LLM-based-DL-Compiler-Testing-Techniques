
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value, dropout_p=0.2, scale_factor=1e-6):
        qk  = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk * scale_factor 
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output  = dropout_qk @ value
