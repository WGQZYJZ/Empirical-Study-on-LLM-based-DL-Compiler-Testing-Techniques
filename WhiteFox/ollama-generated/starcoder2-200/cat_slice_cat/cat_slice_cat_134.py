

class Model(torch.nn.Module):
    def __init__(self, input_tensors):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, size):
        v1  = torch.cat(input_tensors, dim=1) # Concatenate the input tensors along dimension 1 
        v2  = v1[:, :size] # Take a slice of the concatenated tensor along dimension 1
        v3  = v1[:, -size:] # Take another slice of the concatenated tensor along dimension 1
        return torch.cat([v1, v2, v3], dim=1)


# Initializing the model
m = Model(input_tensors=[torch.randn(3, size), torch.randn(4, size)])

 # Inputs to the model
size  = 57965085
 
x1  = [torch.randn(2, size-size//2), torch.randn(3, size//2)]
__output__  = m(*x1)


