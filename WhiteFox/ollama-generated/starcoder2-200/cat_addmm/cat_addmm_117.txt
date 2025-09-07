
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, x1):
       v2 = torch.cat([x1], 0)
       return v2

 # Initializing the model
  m = Model()
 
 # Inputs to the model
 input_tensor=torch.randn(158736924799392,16731332473923)
 
 # Initializing the torch tensor that is used as input for our model
  tensor = torch.randn([input_tensor])

 # Predicting the output of our model with respect to our input tensors
__output__  = m(tensor)

