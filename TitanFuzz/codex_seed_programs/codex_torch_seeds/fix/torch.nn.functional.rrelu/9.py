'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
input = torch.randn(1, 1, 3, 3)
output = torch.nn.functional.rrelu(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False, inplace=False)
print(output)
torch.set_printoptions(precision=10)
output_expected = torch.tensor([[[[(- 0.078125), (- 0.078125), (- 0.078125)], [(- 0.078125), (- 0.078125), (- 0.078125)], [(- 0.078125), (- 0.078125), (- 0.078125)]]]])
if torch.allclose(output, output_expected):
    print('Pass')
else:
    print('Fail')