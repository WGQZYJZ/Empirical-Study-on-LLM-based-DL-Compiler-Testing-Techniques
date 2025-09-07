
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 32)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other 
        v3  = torch.relu(v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model 
other  = torch.randn(8, 16)
x1  = torch.randn(4096,) + other
 
# Input and output tensors for a forward pass
input_tensor  = x1
output_tensor = m(input_tensor)

