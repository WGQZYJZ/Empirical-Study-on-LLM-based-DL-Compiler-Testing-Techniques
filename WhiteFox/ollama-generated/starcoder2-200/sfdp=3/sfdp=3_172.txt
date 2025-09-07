
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, query, key, value):
        v1 = torch.matmul(query, key.transpose(-2, -1))
        v2  = v1 * scale_factor
        v3  = v2.softmax(dim=-1) 
        v4 = self.drop(v3) # Dropout is not implemented here
        v5 = v4.mm(value)  
        return v5
 
# Initializing the model
m  = Model()

