
class Model(torch.nn.Module):
    def __init__(self, keysize=256):
        super().__init__()
        self.key  = torch.nn.Parameter(torch.empty(3, keysize))
 
    def forward(self, query, key):
        value  = torch.randn((10, 4096), dtype=torch.float)
        scale_factor  = (query**2).sum().sqrt()
        invscalef  = float(keysize)/scale_factor
 
        v1  = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1.div(invscalef)
        v3  = v2.softmax(dim=-1)
        v4  = torch.nn.functional.dropout(v3, p=0.5)
        v6  = v4.matmul(value)
 
        return v6

# Initializing the model
keysize  = 9987
m  = Model(keysize).cuda()
 
# Inputs to the model