
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor 
        v3 = torch.relu(v2)

        return v3

# Initializing the model
m = Model()

 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
 __output__  = m(x1)
 
 # Other input tensor for the model 
 other_tensor = torch.zeros(2, 8, 709, 508)

 # The resulting output is a pytorch tensor
 result  = m(other_tensor)

 