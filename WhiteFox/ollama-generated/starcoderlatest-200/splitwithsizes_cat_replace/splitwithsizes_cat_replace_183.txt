
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [1], dim=1) # Split the input tensor along dimension 1 (along axis 1 of shape (3, 64, 64)) and perform shape inference for output.
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate the split tensors along dimension 1 (along axis 1 of shape (3, 64, 64)) and perform shape inference for output.
        return concatenated_tensor


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
