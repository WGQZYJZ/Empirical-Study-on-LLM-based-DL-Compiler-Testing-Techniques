 after optimization
class Model_2(torch.nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, (64,), dim=1) # Split the input tensor along dimension 1 using a 1-element tuple
        concatenated_tensor = torch.cat(split_tensors, dim=1) # Concatenate the split tensors along the same dimension again
        return concatenated_index


