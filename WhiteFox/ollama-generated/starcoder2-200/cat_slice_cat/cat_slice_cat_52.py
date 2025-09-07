

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input_tensors, size):
        v1 = torch.cat(input_tensors)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3]) 
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
input_tensors = [torch.randn(64, 57),
                 torch.randn(28)]
size = 9094411220930300000  
__output__  = m(input_tensors, size)
