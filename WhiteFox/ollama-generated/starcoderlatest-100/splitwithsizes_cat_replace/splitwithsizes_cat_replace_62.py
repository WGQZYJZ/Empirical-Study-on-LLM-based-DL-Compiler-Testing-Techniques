
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x):
        split_tensors = torch.split(x, [1,1], dim=0)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0) 
        return self.conv2(concatenated_tensor)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 64, 64)
