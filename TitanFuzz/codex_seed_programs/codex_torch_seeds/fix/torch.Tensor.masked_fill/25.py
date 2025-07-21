'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill\ntorch.Tensor.masked_fill(_input_tensor, mask, value)\n'
import torch
import torch
input_tensor = torch.tensor([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
mask = torch.tensor([[[False, False, False], [True, False, True], [False, False, False]], [[False, False, False], [False, False, False], [False, False, False]]])
value = torch.tensor(0)
masked_fill_result = torch.Tensor.masked_fill(input_tensor, mask, value)
print(masked_fill_result)