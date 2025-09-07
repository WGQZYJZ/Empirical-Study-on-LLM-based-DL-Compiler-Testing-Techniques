
class Model(torch.nn.Module):
    def __init__(self, size1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = torch.split(x1, size1, dim = 0)
        v2 = [i * 0.5 for i in v1] # apply constant 0.5 to all split tensors along the dimension that has size 0
        v3 = []
        for vi in v2:
            v3.append(vi * 0.7071067811865476) # apply constant 0.7071067811865476 to all split tensors along the dimension that has size 0
        v4 = torch.stack([torch.erf(vi) for vi in v3]) # apply the error function to all split tensors along the dimension that has size 0
        v5 = torch.cat([i * j for i, j in zip(v2, v4)], dim=0) + 1 # add 1 to all split tensors along the dimension that has size 0 
        return torch.stack([vi * jj for vi, jj in zip(v2, v5)]) # multiply all split tensors along the dimension that has size 0 by the output of its error function 


# Initializing the model
m = Model(4)


