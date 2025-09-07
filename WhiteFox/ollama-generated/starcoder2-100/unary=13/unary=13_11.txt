
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1  = torch.nn.Linear(784, 512) 
        self.linear2  = torch.nn.Linear(512, 10) 
 
    def forward(self, x):
        v1  = self.linear1(x)  
        v2  = torch.sigmoid(v1)   
        v3  = v2 * v1        
        return v3


# Initializing the model