
class Model(torch.nn.Module):
    def __init__(self, splitDim=1):
        super().__init__()
 
    def forward(self, x1):
        # Initialize the torch.split/torch.cat objects
        splitters = [torch.split] * 32
        concatenators = [torch.cat] * 32
 
        # Split and concatenate the input tensor along a specific dimension
        v1 = concatenators[0]([splitters[i](x1, 514) for i in range(len(splitters))], dim=splitDim)
        return v1


# Initializing the model