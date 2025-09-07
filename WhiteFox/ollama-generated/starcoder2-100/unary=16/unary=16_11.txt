
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32000, 512)
 
    def forward(self, x1): 
        v1  = self.linear(x1) # linear transformation applied to the input tensor
        v2  = F.relu(v1) # ReLU activation function applied to the output of the linear transformation
        return v2


# Initializing the model