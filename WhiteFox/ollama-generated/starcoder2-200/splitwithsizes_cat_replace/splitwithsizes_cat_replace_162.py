
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x):
        split_tensors  = torch.split(x, [54], dim=-2) # Split the input tensor into a single slice along the last dimension
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(1)], dim=-2) # Concatenate this single slice with the original input tensor
        return concatenated_tensor


# Initializing the model
m  = Model()
 
x1  = torch.randn(1, 3, 64, 87)
__output__  = m(x1)