
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensor_sizes = [64, 64] # The dimension along which the input and output tensors are split in the first operation of each `torch.split` operation
        concatenated_tensor = torch.cat([
            torch.split(x1, split_tensor_sizes, dim=0),  # Split tensor of shape [batch_size, n_channel, height_in, width_in]
            torch.split(input_tensor, split_tensor_sizes, dim=0),
        ], dim=0)  # Concatenate the split tensors along the same dimension
        return concatenated_tensor


# Initializing the model
m = Model()


