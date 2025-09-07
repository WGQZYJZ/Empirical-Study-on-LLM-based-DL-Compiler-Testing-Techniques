
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        splitted = torch.split(input1, [32], 0)
        concatenated = torch.cat([splitted[i] for i in range(len(splitted))], dim=0)
 
        return concatenated

 # Initializing the model
 m  = Model()
 
 # Inputs to the model 
 input1 = torch.randn(64, 32, 85*75*1)
  