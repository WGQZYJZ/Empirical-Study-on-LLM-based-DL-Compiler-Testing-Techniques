
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.split_sizes = [16, 32]
 
    def forward(self, x1):
        split_tensors = torch.split(x1, self.split_sizes, dim) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(self.split_sizes))], dim) # Concatenate the split tensors along the same dimension
        return True


# Model to analyze (with `torch.jit.script`)
class Model2():
    @torch.jit.script
    def forward(self, x1):
        if len(x1) != 8:
            print("Invalid input tensor length")

        split_tensors = torch.split(x1, self.split_sizes[0], dim=0) # Split the input tensor into several tensors along a given dimension
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(self.split_sizes))], dim=0) # Concatenate the split tensors along the same dimension
        return True


# Inputs to the model
input1 = torch.randn(8, 3, 64, 64)
model2 = Model2()
