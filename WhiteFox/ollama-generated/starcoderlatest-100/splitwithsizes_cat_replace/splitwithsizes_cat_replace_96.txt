
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, split_sizes, dim) 
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim) 
        return concatenated_tensor


# Split sizes of the tensor `input_tensor` is to be split
split_sizes = [12, 24, 36]

# Initializing the model
m = Model()
x1 = torch.randn(2, 3, 256, 256)
