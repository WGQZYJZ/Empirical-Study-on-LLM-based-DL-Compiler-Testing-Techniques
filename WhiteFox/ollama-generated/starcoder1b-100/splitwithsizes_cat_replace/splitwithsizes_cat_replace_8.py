
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_sizes = [x1.shape[i] for i in range(x1.ndim)] # Get the number of tensors along a given dimension from each input tensor
        concatenated_tensor = torch.cat([torch.split(input_tensor[i], split_sizes[i], dim=i)
                                     for i in range(len(input_tensor))])  # Concatenate split tensors along a given dimension
