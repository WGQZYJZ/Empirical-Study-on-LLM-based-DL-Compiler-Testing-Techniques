
class Model(torch.nn.Module):
    def __init__(self, n1=256):
        super().__init__()
        self.linear = torch.nn.Linear(n1**3, 4096)
 
    def forward(self, input_tensor):
        split_tensors  = torch.split(input_tensor, int(len(input_tensor)/8), dim=2) # Input tensor is split into 8 equal tensors along the dimension 2 (dimension 1 and 3 are not equal so it will cause an error to split).
        concatenated_tensor  = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=0) # Concatenate all 8 split tensors along the dimension 0 (dimension 1 and 3 are not equal so it will cause an error to concatenate).
        return self.linear(concatenated_tensor)


