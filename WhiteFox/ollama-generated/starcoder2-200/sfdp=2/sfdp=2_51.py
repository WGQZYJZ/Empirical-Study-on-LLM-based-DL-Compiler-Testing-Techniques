
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
 
        inv_scale = 0.25
        
        qk  = torch.matmul(q1, k1.transpose(-2,-1))
        scaled_qk = qk / (inv_scale)
        softmax_qk = scaled_qk.softmax(dim=-1)
        
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.5)
        
        output = dropout_qk @ v1
        
        return output


# Initializing the model
m  = Model()

 # Inputs to the model
 
query  = torch.randn(32,  64)
key    = torch.randn(32,  8 ,  64)
value  = torch.randn(32,  8 ,  64)
 
 