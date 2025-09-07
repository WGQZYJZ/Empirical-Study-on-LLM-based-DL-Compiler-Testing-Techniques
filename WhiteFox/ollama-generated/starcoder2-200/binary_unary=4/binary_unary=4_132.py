
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v2  = torch.relu(x1 + other) # Apply ReLU to the output of the linear transformation plus another tensor
        return v2

