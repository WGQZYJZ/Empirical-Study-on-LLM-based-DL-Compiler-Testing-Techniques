
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, q1, k1, v1):
 
        # q1 = [b, dq, h]
        # k1 = [b, dk, h]
        # v1 = [b, dv, h]
        
        scale_factor  = torch.tensor([[0.79]])
        dropout_p  = torch.tensor(0.5)
 
        v2 = torch.matmul(q1, k1.transpose(-2,-1))
        v3  = v2 * scale_factor
        v4 = v3.softmax(dim=-1)
        v5 = torch.nn.functional.dropout(v4, p=dropout_p) # p: probability that each element will be zeroed. 
        v6  = v5.matmul(v1)
        
        return v6
        

# Initializing the model
m = Model()


# Inputs to the model
q1  = torch.randn(2, 3072, 4) # [b, dq, h]
k1  = torch.randn(2, 3072, 64) # [b, dk, h]
v1  = torch.randn(2, 64, 8)  # [b, dv, h]
 
 __output__  = m(q1, k1, v1)

