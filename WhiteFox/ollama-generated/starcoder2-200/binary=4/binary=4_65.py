
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self._other = torch.zeros([32], dtype=torch.float)
 
    def forward(self, x1):
        
        v1  = torch.nn.functional.linear(x1, self._other)
        return v1 + other


# Initializing the model with an input tensor of 0s
m  = Model()
 
input_tensor = torch.zeros([32, 5], dtype=torch.float)
 
 # Initializing the keyword argument "other" to a random value
other = torch.rand(32) 
 
# Running inference on m with input tensor and keyword argument other
