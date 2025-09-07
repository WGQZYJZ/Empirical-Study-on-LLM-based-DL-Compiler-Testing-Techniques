
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query1, key1, value1):
        v2  = torch.matmul(query1, key1.transpose(-2, -1)) 
        v3 = v2 / inv_scale_factor 
        v4 = v3.softmax(dim=-1)
        v5  = torch.nn.functional.dropout(v4, p=0.1)
        v6  = v5.matmul(value1)  
        return v6

# Initializing the model
m = Model()

 # Inputs to the model