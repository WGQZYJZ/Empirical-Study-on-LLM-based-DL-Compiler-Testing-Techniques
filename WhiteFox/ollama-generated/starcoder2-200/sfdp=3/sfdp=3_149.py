
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale = 0.3 
        self.dropout = torch.nn.Dropout(p=0)
 
    def forward(self, query, key, value):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale)
        softmax_qk = scaled_qk.softmax(dim=-1) 
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=self.dropout)
        output  = dropout_qk.matmul(value)
        return output

# Initializing the model
m  = Model()

 # Inputs to the model
q = torch.randn(64, 80, 512)
k = torch.randn(64, 80, 512)
v = torch.randn(64, 80, 512)
__output__  = m(q, k, v)

