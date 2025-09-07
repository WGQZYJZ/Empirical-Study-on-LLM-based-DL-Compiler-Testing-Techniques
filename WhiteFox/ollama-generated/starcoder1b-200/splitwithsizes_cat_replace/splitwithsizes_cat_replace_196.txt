
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensor0 = torch.split(x1, [3], dim=0)  # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensor0[i] for i in range(len(split_tensor0))], dim=0)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


