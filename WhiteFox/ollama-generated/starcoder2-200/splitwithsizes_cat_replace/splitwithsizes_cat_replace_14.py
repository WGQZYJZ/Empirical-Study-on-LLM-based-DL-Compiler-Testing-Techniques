
class Model(torch.nn.Module):
    def __init__(self, split_size=2):
        super().__init__()
 
    def forward(self, input1, input2):
        v0 = torch.split(input1, split_sizes=[5], 1) # Split the input tensor along dimension 1 with sizes [5] using `torch.split`
        v1 = torch.split(input2, split_size[1], 1)[-1] # Split the second input tensor using `torch.split`, then select the last split
        return v0 + [v1]

# Initializing the model