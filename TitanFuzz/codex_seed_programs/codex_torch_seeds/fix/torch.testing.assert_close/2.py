'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.testing.assert_close\ntorch.testing.assert_close(actual, expected, *, allow_subclasses=True, rtol=None, atol=None, equal_nan=False, check_device=True, check_dtype=True, check_stride=False, check_is_coalesced=True, msg=None)\n'
import torch
input_data = torch.rand(3, 3)
torch.testing.assert_close(input_data, input_data, rtol=0.0001, atol=0.0001)