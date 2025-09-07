
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, size_1):
        t1 = torch.cat([x1, torch.ones_like(x1)], dim=1) # Concatenate input tensor and all ones tensor along dimension 1
        t2 = t1[:, :size_1] # Slice the concatenated tensor along dimension 1
        t3 = t2[:size] # Further slice the tensor along dimension 1
        t4 = torch.cat([t1, t3], dim=1) # Concatenate the original concatenated tensor and the sliced tensor along dimension 1
        return t4


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(20, 3, 64, 64)
size_1 = int(np.ceil(len(x1.view(-1)) ** (1/2))) # Calculate the size of sliced tensor based on the length of all tensors in the list
