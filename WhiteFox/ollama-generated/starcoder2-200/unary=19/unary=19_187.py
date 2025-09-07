
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32*64**2, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1) # Applying linear transformation to the input tensor 
        v2 = torch.sigmoid(v1) # Applying sigmoid function to the output of linear transformation   
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 64*32)


__output__  = m(x1)

# Please also generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements. Plus, please also generate the input tensor for the newly generated model. The model should be different from the previous one.