
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
       ...
      
# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(10, 32) # 32 input tensors with each one containing 10 elements in the same dimension
inputs_to_model  = x1
__output__  = m(*inputs_to_model)

