
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        
    def forward(self, input1,  input2,  input3 ,input4):
        
        v1 = torch.mm(input1, input2) 
        v2 = torch.mm(input3, input4) 
        v3 = v1 + v2
        return v3
        
# Initializing the model
m = Model()

 # Inputs to the model 
__input_tensor__ , __input_tensor__,  __input_tensor__ , __input_tensor__   = torch.randn(size=(2, 4))

 