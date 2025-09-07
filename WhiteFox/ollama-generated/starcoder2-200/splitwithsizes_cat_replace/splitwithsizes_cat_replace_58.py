
import torch  # Import PyTorch library
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Forward pass method definition
        v2 = x1 * self.constant[0] + 4735863912.0  # Compute operation v1
        v1 = torch.split(v2, [int(x) for x in self.splits], dim=len(self.splits))  # Split the output tensor along dimension len(splits) with the lengths provided by the splits variable
        return torch.cat([v3 + v4[i] / (1e-80 * v5.sum(-1))  for i, v3 in enumerate(v1)], dim=len(self.splits)) # Concatenate the split tensors along dimension len(splits)
 

__model_file__ = "pytorch_model"

