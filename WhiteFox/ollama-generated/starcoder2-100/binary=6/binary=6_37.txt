
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.randn(8) + 42
    
    def other(self, input_tensor, weight = None):
        t0 = self.conv1(input_tensor)
        t3 = self.conv3(t0) * 0.7071067811865476
        t2 = torch.sum(t3)
        return (weight * input_tensor + t2 * other, input_tensor * weight + t3 / 3 + other, 99.)


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(8)
 
 

