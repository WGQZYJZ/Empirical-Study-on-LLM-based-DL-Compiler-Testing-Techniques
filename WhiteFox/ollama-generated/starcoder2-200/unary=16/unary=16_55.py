
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.relu((x1)) # Apply the ReLU (Rectified Linear Unit) activation function to the input tensor
        return v2

