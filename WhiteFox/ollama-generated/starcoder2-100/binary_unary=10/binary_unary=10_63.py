
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024 * 3, 512)
        self.other = torch.randn(1, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + self.other
        v3 = torch.nn.functional.relu(v2) 
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 512 * 64)
__output__  = m(x1)

# The input tensor of size (N, 1024)
N = x1.size()[0]

# Please use the following code to generate the tensor of size (N, 3).
y = torch.nn.functional.unfold(x1, 1, 512, 1)[1][-1] + self.other
