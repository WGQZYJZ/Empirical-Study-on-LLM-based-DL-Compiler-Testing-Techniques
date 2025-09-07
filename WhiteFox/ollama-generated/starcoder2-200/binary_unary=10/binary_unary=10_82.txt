
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32768, 4096)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Linear transformation to the input tensor 
        v2  = v1 + other_tensor  
        v3  = F.relu(v2) # ReLU activation function applied to the result of adding another tensor and applying a linear transformation. 
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(64, 32768)
other_tensor  = torch.randn(64, 32768)
__output__   = m(x1)