
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(3, 8) 
        self.key   = torch.nn.Linear(8, 3)
        self.value = torch.nn.Linear(3, 24)
        self.scale_factor = math.sqrt(self.key.weight.shape[-1])
        self.softmax    = torch.nn.Softmax(-1)
        self.dropout   = torch.nn.Dropout(0.5)
    
    def forward(self, x):
        v1  = self.query(x) 
        v2  = self.key(v1)  
        v3  = v2.transpose(-2, -1)  
        v4  = torch.matmul(v1, v3).div(inv_scale_factor)   
        v5  = self.softmax(v4)
        v6  = self.dropout(v5)
        v7  = self.value(x)    
        v8  = v6.matmul(v7)
        return v8

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(3, 32, 32)  
 __output__  = m(x1)
 
