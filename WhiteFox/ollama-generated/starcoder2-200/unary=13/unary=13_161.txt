

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(784, 128)
 
    def forward(self, x): 
        v1  = self.linear(x)  
        v2  = torch.sigmoid(v1)  
        return v2 * v1

m  = Model()

 # Inputs to the model 
 input_tensor=torch.randn(64,784)  
 __output__  = m(input_tensor)
