
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        self.split_tensor = torch.split(x1, 64, dim=0) # Split the input tensor into several tensors along dimension 0 of the input tensor
        v1 = torch.cat([self.split_tensor[i] for i in range(len(self.split_tensor))], dim=0) # Concatenate the split tensors along dimension 0 of the input tensor
        self.split_tensor2 = torch.split(x2, 64, dim=1) # Split the input tensor into several tensors along dimension 1 of the input tensor
        v2 = torch.cat([self.split_tensor2[i] for i in range(len(self.split_tensor2))], dim=1) # Concatenate the split tensors along dimension 1 of the input tensor
        return v1 + v2


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
x2 = torch.randn(4, 8, 64, 64)
