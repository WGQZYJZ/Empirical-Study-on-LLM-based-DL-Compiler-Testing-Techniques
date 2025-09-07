
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        # The following line is added by you.
        inv_scale = 0.1
        
        qk  = torch.matmul(query, key.transpose(-2, -1)) 
        scaled_qk  = qk / (inv_scale)
        softmax_qk  = scaled_qk.softmax(dim=-1)  
        dropout_qk  = torch.nn.functional.dropout(softmax_qk, p=0.4)
        output  = dropout_qk @ value
        return output


# Initializing the model
m  = Model()


# Inputs to the model
query  = torch.randn(8, 32, 512)
key  = torch.randn(8, 32, 512)
value  = torch.randn(8, 64, 512)
 
__output__   = m(query, key, value)