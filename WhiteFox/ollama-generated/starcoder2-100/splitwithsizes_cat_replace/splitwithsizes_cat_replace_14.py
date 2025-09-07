
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
      	split_tensors  = torch.split(x1, [20], 3)
      	return torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=3), torch.sum(split_tensors)
 
# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(5, 40, 29, 86)
 
 # Initializing the inputs that trigger the detection of interest.
inputs = [torch.randn(37, 40, 13, 78)]
 
__output__, __sum__ = m(*inputs)

