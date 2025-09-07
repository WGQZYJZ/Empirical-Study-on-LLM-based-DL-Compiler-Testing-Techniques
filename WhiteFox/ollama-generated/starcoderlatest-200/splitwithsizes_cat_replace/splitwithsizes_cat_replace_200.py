
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, 3, dim=0)
        concatenated_tensor = torch.cat(split_tensors, dim=0)
 
        return True


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
