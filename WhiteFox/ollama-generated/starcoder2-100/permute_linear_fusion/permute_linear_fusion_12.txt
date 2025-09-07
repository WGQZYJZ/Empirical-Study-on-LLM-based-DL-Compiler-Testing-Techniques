
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1).permute(0, 1, 3) # Permute the input tensor to a shape like (batch, in_channel, height, width), then swap the last two dimensions of this tensor with batch and in_channel dimension
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) # Apply linear transformation to the permuted input tensor
        return v2

# Initializing the model