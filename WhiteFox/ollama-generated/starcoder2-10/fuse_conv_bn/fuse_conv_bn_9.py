
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv2 = torch.nn.Conv2d(1, 30, kernel_size=5) 
        self.conv4 = torch.nn.Conv3d(30, 64, kernel_size=5) 
        self.bn = torch.nn.BatchNorm3d(num_features=64)
        self.linear = torch.nn.Linear(8713920, 2)

    def forward(self, x):
      v1 = torch.nn.functional.conv2d(x, weight=self.conv2.weight) 
      v2 = self.conv4(v1) # X can be 1, 2, or 3 representing the dimension
      output = torch.nn.functional.linear(v2, self.linear.weight, self.linear.bias) 
      return output

# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(100, 30, 480, 640) 

__output__   = m(x)

<img src="images/Model_Conv3d_and_Linear_Fused.png" alt="Drawing" style="width: 576px;"/>

