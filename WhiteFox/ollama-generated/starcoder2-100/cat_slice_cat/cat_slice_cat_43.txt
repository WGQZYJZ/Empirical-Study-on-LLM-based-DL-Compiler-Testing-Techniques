
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, inputs, size): 
        v1 = torch.cat(inputs)  
        v2 = v1[:, :size]
        return  torch.cat([v1, v2], dim=1)

# Initializing the model
m = Model()

 # Inputs to the model
    inputs_0 = torch.randn(856437971912854247535353333, 3, 370)
     inputs_1 = torch.randn(24755043182882702147835677209, 3, 418)
     inputs_2 = torch.randn(45430437559375993531213010071, 3, 393)
     inputs_3 = torch.randn(32652568127135576335704703174, 3, 383)
     inputs_4 = torch.randn(98743011358777380325095012317, 3, 365)
# Input to the model
    size = torch.LongTensor([723])
__output__  = m([inputs_0],size[0] ,inputs_[4], inputs_[3],inputs_[2],inputs_[1],inputs_[0])
