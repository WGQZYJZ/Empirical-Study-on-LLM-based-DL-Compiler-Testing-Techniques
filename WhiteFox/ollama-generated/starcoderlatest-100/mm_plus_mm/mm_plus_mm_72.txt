
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.nn.Linear(256, 50)
        self.input2 = torch.nn.Linear(256, 50)
 
    def forward(self, x1, x2):
        v1 = self.input1(x1) # Linear transformation applied to the input tensor 
        v2 = self.input2(x2) # Linear transformation applied to the input tensor 
        v3 = torch.mm(v1, v2) # Matrix multiplication between the two outputs of the linear transformations
        return v3

# Inputs to the model
x1 = torch.randn(1, 256) 
x2 = torch.randn(1, 256)
