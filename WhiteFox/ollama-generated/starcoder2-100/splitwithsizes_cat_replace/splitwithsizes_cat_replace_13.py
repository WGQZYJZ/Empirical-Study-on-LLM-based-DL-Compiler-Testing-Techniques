
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_op = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = x1
        v1 = torch.split(v1, split_sizes=[7], dim=3)[0] # Split the input tensor into several tensors along a given dimension
        v2  = self.split_op(x1)  # Apply a convolution operation to each of these new tensors
        v4  = torch.cat([v2[i] for i in range(len(split_sizes))], dim=3) 
        return v4

# Initializing the model
m  = Model()

