
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=7, stride=1)
        self.linear1 = torch.nn.Linear(8*40*40, 64)

    def forward(self, x):
        v1  = self.conv1(x) # Apply pointwise convolution with kernel size 7 to the input tensor 
        v2  = v1 + other_tensor  # Add another tensor to the output of the convolution
        v3  = torch.flatten(v2, start_dim=0, end_dim=-1) # Flatten the output of the convolution (note that "start_dim" and "end_dim")
        v4  = self.linear1(v3) # Apply a linear transformation to flattened output
        return v4

# Initializing model
m  = Model()
other_tensor  = torch.randn(20,8*40*40).cuda()
 
# Input tensor of size (20, 3, 64, 64) to the model
x1  = torch.rand(20, 3, 64, 64).cuda()
__output__  = m(x1)

