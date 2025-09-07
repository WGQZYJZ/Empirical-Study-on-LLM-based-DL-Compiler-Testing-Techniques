
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       split_tensors = torch.split(x1, [32], 0) # Split the input tensor into two tensors with sizes of 32 and 48, respectively along dimension 0
       concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], 0)  # Concatenate the split tensors along axis 0
        return torch.mean(torch.max(concatenated_tensor), [1, 2])


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(48, 3, 64, 64)


