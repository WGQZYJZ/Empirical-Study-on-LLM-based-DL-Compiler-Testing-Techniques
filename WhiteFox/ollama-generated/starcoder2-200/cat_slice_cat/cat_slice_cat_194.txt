
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, size=4096):
        v1 = torch.cat([x1, x2], dim=1)
        v2  = v1[:, 0:size] # This is the only difference from the previous model example
        v3 = v2[:, 0:size] 
        v4  = torch.cat([v1, v3], dim=1)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model (the first input is the input of the first model, and the second is an additional input for generating the sliced tensor.)
x1  = torch.randn(1024, size=4096)
x2  = torch.randn(size=735)

 # Generating the output (the second element in the tuple is the output of the model after its slicing operation along dimension 1)
