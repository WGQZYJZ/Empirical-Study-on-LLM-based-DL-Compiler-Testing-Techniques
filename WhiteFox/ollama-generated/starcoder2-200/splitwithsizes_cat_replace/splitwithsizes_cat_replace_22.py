
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        # Split the input tensor into two tensors along axis 0 and one tensor along axis 1:
        split_tensors = torch.split(x1, 2, dim=0)
        # Concatenate these split tensors along dimension 0:
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=0)
        return concatenated_tensor
 
 
m = Model()
 
# Inputs to the model
x1 = torch.randn(2, 3, 4, 5) # Input tensor of shape (2, 3, 4, 5)
