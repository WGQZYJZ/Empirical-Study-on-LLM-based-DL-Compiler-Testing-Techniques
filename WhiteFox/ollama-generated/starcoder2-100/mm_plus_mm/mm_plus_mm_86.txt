
class Model(torch.nn.Module):
    def __init__(self, input1=None, input2=None, input3=None, input4=None):
        super().__init__()
 
    def forward(self, x1, y1, x2, y2):
        v1  = torch.mm(x1, x2) 
        v2  = torch.mm(y1, y2) 
        v3  = v1 + v2  
        return v3 


# Initializing the model and feeding in two tensors for initialization of input parameters `input1` and `input2`. 

m = Model(input1, input2)

 # Inputs to the model