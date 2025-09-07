
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.functional.Linear(768, 768)
 
    def forward(self, q1, k2):
        v1 = torch.nn.functional.linear(q1, k2, bias=None).div_(scale_factor) 
        v2 = v1 + dropout_p.mul(-float("inf")) # Add -infinity to the scaled dot product with dropout applied
        v3  = F.softmax(v2, dim=-1) 
        return torch.matmul(v3, k2)

# Initializing the model
m  = Model()

 # Inputs to the model
 query  = torch.randn(768, 768)
 key   = torch.randn(768, 768)
 
 __output__  = m(query, key)
 
 