
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.linear1  = torch.nn.Linear(2048, 5)
        self.linear2  = torch.nn.Linear(3, 1967*8)
 
    def forward(self, x):
 
        v1  = self.linear1(x) 
        v2  = nn.functional.softmax(v1, dim=0) 
        v3  = self.linear2(v2)
        v4  = v3 * 5  # Apply the error function to the output of the convolution
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1, y1 = torch.randn(5, 3), torch.zeros(3)
