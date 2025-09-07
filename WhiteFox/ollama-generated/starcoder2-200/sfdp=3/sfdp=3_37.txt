

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, k1, v1, q1):
       v2  = torch.matmul(q1, (k1).transpose(-2, -1)) * scale_factor
       v3  = v2.softmax(dim=-1)
       v4  = torch.nn.functional.dropout(v3, p=dropout_p)
       __output__   = v4 @ v1
       return __output__

# Initializing the model and inputs to the model
m = Model()
x1  = torch.randn(128, 64, 500) # Query tensor shape [batch size, query depth, query length]
k1  = torch.randn(128, 64, 500) # Key tensor shape [batch size, key depth, key length]
v1  = torch.randn(128, 397, 500)# Value tensor shape [batch size, value depth, value length]

