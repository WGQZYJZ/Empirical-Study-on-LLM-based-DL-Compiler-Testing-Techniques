'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lu_solve\ntorch.Tensor.lu_solve(_input_tensor, LU_data, LU_pivots)\n'
import torch
input_tensor = torch.tensor([[2.0, 1.0, 1.0], [1.0, 3.0, 2.0], [1.0, 0.0, 0.0]], dtype=torch.float32)
(LU_data, LU_pivots) = input_tensor.lu()
output_tensor = torch.Tensor.lu_solve(input_tensor, LU_data, LU_pivots)
print('Output Tensor:')
print(output_tensor)