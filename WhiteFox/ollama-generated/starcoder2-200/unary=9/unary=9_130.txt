
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Addition operation
        v3  = torch.clamp_min(v2, 0)# Clamp the addition to a minimum of 0
        v4  = torch.clamp_max(v3, 6) # Clamps the previous addition by clamping it down to 6
        v5  = v4 / 6# Divides the clamped value with 6
        return v5

# Initializing the model
m1 = Model()


# Inputs to the model 1
x1_1 = torch.randn(2, 3, 60, 60)
__output___ = m1(x1_1)
 
# Input 2 for the model with clamp_min/clamp_max
x1_2 = torch.tensor([[7.,8.],
                     [9.,-4],
                     [-5,-3]]) # Creates a two dimensional tensor that contains the elements of [-5, -3] and [7,8]

x1_3 = torch.tensor([[-6., 0],
                     [-2,-20]])

