
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [x1.shape[0]//2, x1.shape[0]//2+1]
        concatenated_tensor = torch.cat([
            torch.split(input_tensor, split_sizes[i], dim) for i in range(len(split_sizes))
        ], dim=1)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


