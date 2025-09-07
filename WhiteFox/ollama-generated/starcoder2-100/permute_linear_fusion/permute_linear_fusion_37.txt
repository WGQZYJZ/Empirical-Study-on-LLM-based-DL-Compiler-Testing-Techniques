
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 3)

    def forward(self, x1):
        v1  = x1 .permute(0 , 1, 4).reshape((16 * 4, 8)) # Permute the input tensor
        v2  = self.linear(v1) + torch.nn.functional.conv2d(self.linear.weight, v1.shape[0]) 
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(4 ,8 ,16) 
 