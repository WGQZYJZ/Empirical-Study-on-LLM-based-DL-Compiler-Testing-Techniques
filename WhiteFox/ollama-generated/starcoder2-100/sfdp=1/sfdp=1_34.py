
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1, dropout_p=0., inv_scale_factor=256*7):
        v1  = torch.matmul(q1, k1.transpose(-2,-1)) / float(inv_scale_factor) # scale_factor 32*4
        softmax_qk = v1.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v1)
        return output


# Initializing the model
m  = Model()
 
# Inputs to the model
q1  = torch.randn(32*4, 7, 64)
k1  = torch.randn(32*4, 7, 64)
v1  = torch.randn(32*4, 7, 8)
 

