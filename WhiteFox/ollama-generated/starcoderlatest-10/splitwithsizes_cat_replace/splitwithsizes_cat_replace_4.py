
class Model(torch.nn.Module):
    def __init__(self, dim=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 3, dim) 
        concatenated_tensor = torch.cat(split_tensors, dim) 
        return concatenated_tensor


# Initializing the model
m = Model(dim=0)

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 