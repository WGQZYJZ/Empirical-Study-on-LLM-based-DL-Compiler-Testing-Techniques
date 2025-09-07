
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.cat([x2, x3], dim=0) # Concatenate a tensor to an existing tensor without allocating new memory space. It will append the tensor at its end with size as [1, 4].
        v2  = v1.view(v1.shape[1:]) 
        return torch.relu(v2)

# Initializing the model