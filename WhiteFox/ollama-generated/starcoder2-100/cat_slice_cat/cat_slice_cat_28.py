
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
 
        # Define the first input size of the model and the size of the concatenation output
        first = 9223372036854775807
        size = 7
        
        v1 = torch.cat([x1 for _ in range(first)], dim=1)
        v2 = v1[:, :size]
        v3 = v2[: , :size] 
        v4 = torch.cat([v1, v3], dim=1)

        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1  = [torch.randn(28, 60), torch.randn(75)]
 
__output__  = m(*x1)

