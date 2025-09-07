
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) - other_tensor 
        v2 = F.relu(v1) # Note: torch.nn.functional.relu is also available as a class attribute.
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
input_tensor  =  torch.randn(3, 64, 64) # Generate input tensor
other_tensor = torch.randn(1).sub(0.5) # Add another random tensor


__output__   = m(input_tensor)

