
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1 = self.linear(x1)
        v2  = v1 + torch.randn(30).cuda() 
        return v2

 # Initializing the model
m = Model()
 
 # Inputs to the model 
 x1 = torch.randn(4587, 69) 

 # Running the model on the input tensors 
 __output__= m(x1)

