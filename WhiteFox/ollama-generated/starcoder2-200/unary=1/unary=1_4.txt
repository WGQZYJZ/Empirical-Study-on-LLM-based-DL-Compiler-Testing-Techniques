
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(8, 3)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1  *  0.5 
        v3  = (v1  *  v1  *  v1 )  +   0.044715  
        v4  = torch.tanh((torch.erf(v3)*-1)) 
        return v4

# Initializing the model<|end_of_code|>
m  = Model()

