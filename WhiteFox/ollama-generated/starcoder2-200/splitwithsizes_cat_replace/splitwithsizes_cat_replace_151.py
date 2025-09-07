
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.split_tensor = torch.nn.Identity()
 
    def forward(self, x1):

        # Split the input tensor into several tensors along a given dimension 
        split_tensors  = torch.split(x1, [32] * 8 + [64], dim=0)
 
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=0)

        return concatenated_tensor, self.split_tensor(x1)


# Initializing the model with inputs
x1 = torch.randn(8 * 32 + 64, 3, 5, 5)
 
m = Model()
output, splitted_tensor  = m(x1)

print(f"The shape of the concatenated tensor: {output.shape}")
