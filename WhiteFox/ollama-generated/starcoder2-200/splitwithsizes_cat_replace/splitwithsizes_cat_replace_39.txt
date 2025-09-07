

import torch  # pylint: disable=unused-import, ungrouped-imports, import-error
 
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, [320], 1) 
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], 1)
        return concatenated_tensor
