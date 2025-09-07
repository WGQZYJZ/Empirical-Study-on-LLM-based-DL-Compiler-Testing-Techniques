
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_qk = torch.matmul(query, key.transpose(-2, -1)) / 3072.0
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=0.156) # 156 is not a prime number
        output  = dropout_qk.matmul(value)
        return output


# Initializing the model
m  = Model()
 
# Inputs to the model
q  = torch.randn(8, 49360)
k  = torch.randn(512, 72930).t().div_(math.sqrt(49360))
v  = torch.randn(8, 512)
 
__output__  = m(q, k, v)

