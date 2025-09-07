
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.conv2  = torch.nn.Conv2d(56,70,3)
 
    def forward(self, x): 
        v1  = self.conv(x) + other
        v4 = torch.relu(v1)
        v2 = torch.max_pool2d(v4, kernel_size=(3, 3), stride=1) # Add another tensor to the output of the convolution
        return torch.flatten(v2, start_dim=1)

# Initializing the model
m = Model()

