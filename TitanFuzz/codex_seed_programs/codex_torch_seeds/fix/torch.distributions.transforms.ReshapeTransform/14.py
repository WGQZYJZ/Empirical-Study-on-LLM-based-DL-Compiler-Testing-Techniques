'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
print(torch.__version__)
input_data = torch.rand(3, 4, 5)
print(input_data.shape)
reshape_transform = torch.distributions.transforms.ReshapeTransform((3, 4, 5), (5, 12))
output_data = reshape_transform(input_data)
print(output_data.shape)