

import torch
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [5], dim=2) # Split the input tensor into 5 subtensors of size 64 by 32 along dimension 0 with stride 1 and padding 0
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], dim=0) # Concatenate these subtensors back to the original size 5 * 64 by 32 along dimension 0 with stride 1 and padding 0
        concatenated_tensor = torch.cat([concatenated_tensor, concatenated_tensor[:, :, :5]], axis=0)
 
        return concatenated_tensor

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1  = torch.randn(32, 64, 30)
  __output__  = m(x1)

