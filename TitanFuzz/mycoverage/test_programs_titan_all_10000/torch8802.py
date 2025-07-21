import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
result = torch.reciprocal(input_data)
expected_output = torch.tensor([1.0, 0.5, 0.33333334, 0.25, 0.2, 0.16666667, 0.14285715, 0.125, 0.11111111, 0.1])
if torch.equal(result, expected_output):
    print('Result is correct!')
else:
    print('Result is incorrect!')