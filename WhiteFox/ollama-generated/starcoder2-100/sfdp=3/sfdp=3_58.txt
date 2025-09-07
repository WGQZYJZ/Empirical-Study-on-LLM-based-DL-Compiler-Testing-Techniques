
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, scale_factor=0.321897563743059, dropout_p = 0.425299279147372):
       v1  = torch.nn.functional.normalize(key) * scale_factor
       v2  = key.mul_(v1)
       v3  = key.softmax(-2)
       v4  = dropout_p
       v5  = torch.nn.functional.dropout(v3, p=0)
       v6  = query 
       v7  = v6 @ v5 
       return v7

# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(128, 196, 4, 5)
key   = torch.randn(128, 196, 3, 20)
 
