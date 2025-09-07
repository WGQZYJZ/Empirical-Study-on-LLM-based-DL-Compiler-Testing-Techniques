
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 3)

    def forward(self, x1, y1):
      v1 = x1.permute(0, 2, 1) # Permute input tensor X
      v2 = torch.bmm(v1, y1.transpose(-2,-1)) 
      return self.linear(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(30, 40, 50) # The shape of x1 is 30 x 50 x 40 (Note that the two tensors may have different sizes or even a variable number of dimensions).
y1 = torch.randn(32, 69, 87)


# Initializing the model with random seeds to ensure reproducibility for testing
m = Model()

x1 = torch.randperm(30*40*50).view(-1,50,40) # The shape of x1 is 30 x 50 x 40 (Note that the two tensors may have different sizes or even a variable number of dimensions).
y1 = torch.randn(x1.size())

