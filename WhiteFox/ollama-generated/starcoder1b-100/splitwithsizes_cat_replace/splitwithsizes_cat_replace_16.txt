
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensor1  = self.conv(x1)  # Split the input tensor into several tensors along dimension 0
        split_tensor2  = self.conv(x1)  # Split the input tensor into several tensors along dimension 1
        concatenated_tensor  = torch.cat([split_tensor1, split_tensor2], dim=0)  # Concatenate the split tensors along the same dimension
        return True


# Initializing the model
m  = Model()
__output__  = m(x1)
