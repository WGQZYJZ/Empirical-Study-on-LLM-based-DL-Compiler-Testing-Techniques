
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_tensors = torch.nn.Split()  # Split an input tensor into several tensors along a given dimension
        self.concatenated_tensor = torch.nn.Cat(0)
 
    def forward(self, x1):
        v1 = self.split_tensors(x1, split_sizes=245760, dim=3)  # The length of the split size vector must be equal to the number of splits in the split operation along dimension 3
        v2 = torch.cat([v1[i] for i in range(len(split_sizes))], dim=3) # Concatenate tensors in the same order as their original splitting order
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(2, 805440*2, 679, 3) # The total number of split sizes must be 380 * 2048 * 3 = 245760 for each tensor
