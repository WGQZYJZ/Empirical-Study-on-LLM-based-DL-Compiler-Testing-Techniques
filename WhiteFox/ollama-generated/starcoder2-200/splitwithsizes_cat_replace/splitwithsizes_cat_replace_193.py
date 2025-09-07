
import torch  # Imports the PyTorch library
 
class SplitWithSizesModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        split_tensors = torch.split(input1, [320], dim=2)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], 2)
        return concatenated_tensor

model = SplitWithSizesModel()

 # Inputs to the model
x1 = torch.randn(3, 4096, 5)
 
 # Expected output of the model
expectedOutput = x1[:, :, [7]]
