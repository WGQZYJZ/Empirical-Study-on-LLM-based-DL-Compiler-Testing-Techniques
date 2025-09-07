
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       conv  = torch.nn.functional.conv2d(x1, ...) 
       vbn  = torch.nn.functional.batchnorm2d(v3) 
        return v4 

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensor  = torch.randn(10, 6)

 