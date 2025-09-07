
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3, input4): 
        v0 = torch.mm(input1, input2)
        v1 = torch.mm(input3, input4) 
        return v0 + v1
# Initializing the model
m  = Model()

 # Inputs to the model