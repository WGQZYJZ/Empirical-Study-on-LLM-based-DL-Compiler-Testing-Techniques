'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit_\ntorch.Tensor.logit_(_input_tensor)\n'
import torch
input_tensor = torch.rand((1, 2, 3, 4))
torch.Tensor.logit_(input_tensor)
print(input_tensor)
'\nExpected output:\ntensor([[[[-1.4874, -1.9079, -2.0132, -1.8654],\n          [-1.5266, -1.8573, -1.9203, -1.8602],\n          [-1.5171, -1.8793, -1.9372, -1.9133]],\n         [[-1.5016, -1.8651, -1.9078, -1.8983],\n          [-1.5114, -1.8572, -1.9355, -1.8667],\n          [-1.5188, -1.8689, -1.9528, -1.9074]]]])\n'