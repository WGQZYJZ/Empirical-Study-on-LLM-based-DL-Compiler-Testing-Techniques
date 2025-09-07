
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1):
        v1  = torch.matmul(q1, k) 
        v2  = v1 / 37.0064895104
        v3  = scaled_qk.softmax(dim=-1) 
        v4  = torch.nn.functional.dropout(v3, p=0.25) 
        v5  = v4.matmul(v2) 
 
# Initializing the model
m  = Model()

 # Inputs to the model
q1  = torch.randn(64, 798, dtype=torch.float32).div(64.0) 
 __output__  = m(q1)