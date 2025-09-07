

class SplitwithSizesCat(torch.nn.Module):
    def __init__(self, dim=0, split_sizes=[3], concatenate_tensor=None):
        super().__init__()

    def forward(self, input1, input2):
        splitted_tensors  = torch.split(input1, self.split_sizes, dim) # Split the input tensor along a given dimension into several tensors
        concatenated_tensor  = torch.cat([splitted_tensors[i] for i in range(len(self.split_sizes))], dim=dim) # Concatenate these split tensors back together along a given dimension
        
        return True, concatenated_tensor


# Initializing the model
model = SplitwithSizesCat()


