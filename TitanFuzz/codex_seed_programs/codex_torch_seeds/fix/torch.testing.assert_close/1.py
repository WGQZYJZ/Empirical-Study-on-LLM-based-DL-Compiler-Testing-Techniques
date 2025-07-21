'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.testing.assert_close\ntorch.testing.assert_close(actual, expected, *, allow_subclasses=True, rtol=None, atol=None, equal_nan=False, check_device=True, check_dtype=True, check_stride=False, check_is_coalesced=True, msg=None)\n'
import torch
import torch
actual = torch.tensor([0.1, 0.2, 0.3])
expected = torch.tensor([0.1, 0.2, 0.3])
torch.testing.assert_close(actual, expected)
actual = torch.tensor([0.1, 0.2, 0.3])
expected = torch.tensor([0.1, 0.2, 0.4])
try:
    torch.testing.assert_close(actual, expected)
except AssertionError as e:
    print(e)
actual = torch.tensor([0.1, 0.2, 0.3])
expected = torch.tensor([0.1, 0.2, 0.4])