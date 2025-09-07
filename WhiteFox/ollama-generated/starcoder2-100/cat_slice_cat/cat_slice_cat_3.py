
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2): 
        v1 = torch.cat([x1], dim=1) # Concatenate the first input along dimension 1. This should be different from the previous example.
        v3_size = int(v1[:,0:9223372036854775807].shape[1]) 
        v3 = torch.cat([x1, x2], dim=1)[: , 0:v3_size] # Take another slice of the concatenated tensor along dimension 1
        v4 = torch.cat([v1, v3], dim=1) # Concatenate the first sliced input along the second sliced input. This should be different from the previous example.
        return v4

# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn(1, 9223372036854775807) # Size of the first input is unknown at runtime
x2 = torch.randn(1, size) # Size of the second input is unknown at runtime

