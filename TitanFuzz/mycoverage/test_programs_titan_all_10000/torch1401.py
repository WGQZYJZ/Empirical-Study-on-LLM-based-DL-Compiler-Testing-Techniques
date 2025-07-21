import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 3, 3)
output = torch.nn.functional.rrelu(input, lower=(1.0 / 8), upper=(1.0 / 3), training=False, inplace=False)
torch.set_printoptions(precision=10)
output_expected = torch.tensor([[[[(- 0.078125), (- 0.078125), (- 0.078125)], [(- 0.078125), (- 0.078125), (- 0.078125)], [(- 0.078125), (- 0.078125), (- 0.078125)]]]])
if torch.allclose(output, output_expected):
    print('Pass')
else:
    print('Fail')