
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [8], dim=1) # Split the input tensor into several tensors along dimension 1
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_sizes))], dim=1) # Concatenate the split tensors along dimension 1
        return concatenated_tensor

# Initializing the model
m = Model()
x2 = x1.unsqueeze(dim=0)

