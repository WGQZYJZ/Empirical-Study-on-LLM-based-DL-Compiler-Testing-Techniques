
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.sigmoid(v1) 
        return v2 

 # Initializing the model 
m  = Model()

 # Inputs to the model 
 x1 = torch.randn(3, 8, 4096 , 571 )
 
