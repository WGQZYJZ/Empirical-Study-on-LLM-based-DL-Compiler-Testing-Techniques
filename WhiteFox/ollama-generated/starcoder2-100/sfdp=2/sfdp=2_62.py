
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
        qk = torch.matmul(q1, k1)
        scale  = 0.5
        scaled_qk = qk / scale
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.32)
        output = dropout_qk @ v1
        return output


# Initializing the model
m  = Model()
 
# Inputs to the model
q1 = torch.randn(64, 8, 512, 512).to(torch.float32)
k1 = torch.randn(64, 8, 512, 512).to(torch.float32)
v1 = torch.randn(64, 8, 512, 512).to(torch.float32)
 
__output__  = m(q1, k1, v1)

