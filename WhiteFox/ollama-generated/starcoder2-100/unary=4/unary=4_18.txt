
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(4,8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1  * 0.5
        v3  = v1  * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1 
        v6  = v2 * v5
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
  x1  = torch.randn(1, 8)
  
  # The size of inputs is (N, 3, 4). Here N is batch_size
  
# Generate 1 valid input tensor and 1 invalid input tensor.

# Valid Input
x2 = torch.tensor([
    [
        [-0.5697],
        [ 0.3974] , 
        [ -2.1782 ]
      ]
  ])
  
 # The size of inputs is (N, 3, 4). Here N is batch_size
  
# Invalid Input
x3 = torch.tensor([
    [
        [-0.5697],
        [ 0.3974] , 
        [-2.1782 ]
      ],
    ])
