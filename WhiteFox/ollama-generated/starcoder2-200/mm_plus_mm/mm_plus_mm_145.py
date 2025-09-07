
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        v1 = torch.mm(x1[0], x2)  # Multiply the input tensor with input tensor x3 to get the output of the model
        v2 = torch.mm(x3, x4)   #Multiply the input tensor with input tensor x5 to get the output of the model
 
        return [v1 + v2]
 

# Initializing the model 
m = Model()
__output__  = m(x6)

