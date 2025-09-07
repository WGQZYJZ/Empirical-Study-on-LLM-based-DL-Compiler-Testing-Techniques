
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        split_sizes = [torch.tensor([1]) for _ in range(v1.shape[0])]
        concatenated_tensor = torch.cat([
            torch.split(v1, split_sizes, dim=-1), # Split the input tensor into several tensors along a given dimension
        ], dim=-1) # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
